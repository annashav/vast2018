#Scripts for metadata visualization
#Incluseds scripts for plotting recordings

#DEPENDENCIES:
#Run install.packages("<Package>") command, if needed.
library(png)
library(plot3D)

#CHANGE TO YOUR DIRECTORY
BASE            <- "C:\\Users\\Andrew\\Documents\\Github\\vast2018\\"
CSV_PATH        <- paste(BASE, "metadata\\AllBirds_Vocalization.csv", sep="")
TEST_BIRDS_PATH <- paste(BASE, "Test Birds Location.csv",     sep="")
IMAGE_PATH      <- paste(BASE, "Lekagul Roadways 2018.png",   sep="")

X_MAX <- 200
Y_MAX <- 200
DUMP  <- c(x=148, y=159) #Location of alleged dump site.
ALL_QUALITIES  <- c("A", "B", "C", "D", "E", "no score")
QUALITY_COLORS <- c("Purple", "Blue", "Green", "Yellow", "Orange", "Black")

ALL_SPECIES    <- c(
 "Bent-beak Riffraff", "Blue-collared Zipper",    "Bombadil",
 "Broad-winged Jojo",  "Canadian Cootamum",       "Carries Champagne Pipit",
 "Darkwing Sparrow",   "Eastern Corn Skeet",      "Green-tipped Scarlet Pipit",
 "Lesser Birchbeere",  "Orange Pine Plover",      "Ordinary Snape",
 "Pinkfinch",          "Purple Tooting Tout",     "Qax",
 "Queenscoat",         "Rose-crested Blue Pipit", "Scrawny Jay",
 "Vermillion Trillian"
)
SPECIES_COLORS <- c(
  "blue",            "brown2",     "black",
  "orange1",         "violet",     "plum2",
  "red3",            "magenta3",   "turquoise",
  "tomato2",         "violetred1", "cyan",
  "burlywood1",      "darkred",    "darkorange4",
  "darkolivegreen4", "deeppink1",  "rosybrown",
  "yellowgreen"
)
names(SPECIES_COLORS) <- ALL_SPECIES

ALL_VOCALIZATIONS <- c(
  "\"call, song\"", "bill-snapping", "call", "drumming", "scold", "song"
)
VOCALIZATION_COLORS <- c(
  "purple", "orange", "blue", "green", "black", "red"
)
names(VOCALIZATION_COLORS) <- ALL_VOCALIZATIONS

dtable <- read.csv(CSV_PATH, header=TRUE)

#Plot the locations of the bird call recordings.
#
#title         - title for plot
#colors        - colors for each (x, y) point
#plot_bg       - T/F whether or not to plot the roadways map
#point_style   - point shape/style
#factory_style - point shape/style
plot_xy <- function(dtable, title, colors, plot_bg=TRUE, point_style=19, dump_style=24)
{
  x <- as.numeric(dtable[["X"]])
  y <- as.numeric(dtable[["Y"]])

  plot(x, y, main=title, xlim=c(0, X_MAX), ylim=c(0,X_MAX), pch=point_style, col=colors)

  #Load and display image image. From StackOverflow.
  if(plot_bg)
  {
    roadways                   <- readPNG(IMAGE_PATH)
    raster                     <- as.raster(roadways[,,1:3])
    raster[roadways[,,4] == 0] <- "white"
    rasterImage(raster, 0, 0, X_MAX,Y_MAX)
  }

  par(new=TRUE) #To make the plot on top of map, instead of making a new plot
  plot(x, y, main=title, xlim=c(0,X_MAX), ylim=c(0,Y_MAX), pch=point_style,
       col=colors)

  par(new=TRUE)
  plot(DUMP["x"], DUMP["y"], main="", xlab="", ylab="", pch=dump_style,
      xlim=c(0,X_MAX), ylim=c(0,Y_MAX))
}

#Filter Templates
#filtered <- dtable[dtable$English_name %in% selected_species,]
#filtered <- filtered[filtered$Quality %in% selected_qualities,]
#filtered <- filtered[filtered$Year %in% selected_years,]

#Generates a series of maps giving all recordings from a given year.
#
#out_dir - Directory to place images
generate_maps <- function(out_dir)
{
  for(year in 1983:2018)
  {
    filtered <- dtable[dtable$Year %in% year,]
    colors   <- SPECIES_COLORS[filtered[["English_name"]]]
    out_file <- paste(out_dir, "AllBirds_", year, ".png", sep="")

    png(out_file)
    plot_xy(filtered, paste("Recordings from", year), colors)
    dev.off()
  }
}

#Generates a series of histograms.
#
#column     - column to use for the histogram
#collection - collection of objects to filter with (for example time or species names)
#filter     - function taking a dataframe and element from the collection to filter table before histogram is made
#breaks     - specifies where the histogram columns go
#ylim       - vector of 2 numbers for the upper and lower bound for the y-axis
#out_dir    - Directory to place images
generate_histograms <- function(dtable, column, collection, filter, breaks, ylim, out_dir)
{
  for(element in collection)
  {
     filtered <- filter(dtable, element)
     title    <- paste("Histogram of", column, "for", element)
     out_file <- paste(out_dir, "Hist_", column, "_", element, ".png", sep="")

     png(out_file)
     hist(filtered[[column]], main=title, xlab=column, ylim=c(0,60), col="lightblue", breaks=breaks)
     dev.off()
  }
}

plot_xy(dtable, "All Species Colored by Recording Quality", QUALITY_COLORS[dtable[["Quality"]]])
#plot_xy(dtable, "All Species Colored by Call Type", VOCALIZATION_COLORS[dtable[["Vocalization_type"]]])
#Generate histogram of all data
#hist(dtable[["Year"]], main="Histogram of Year of Recording", xlab="Year", col="lightblue", breaks=1983:2018)
#hist(dtable[dtable[["Month"]] != 0,][["Month"]], main="Histogram of Month of Recording", xlab="Month", col="lightblue", breaks=1:12)
#hist(dtable[["Hour"]], main="Histogram of Hour of Recording", xlab="Hour", col="lightblue", breaks=0:23)

#Histogram of year, number of recordings from before April
#beforeMarch <- dtable[dtable[["Month"]] <= 3, ]
#hist(beforeMarch[["Year"]], main="Histogram of Years from Jan to Mar", xlab="Year", ylim=c(0,60), col="lightblue", breaks=1983:2018)
#table[beforeMarch[["Year"]])

filter1 <- function(dtable, specie)
{
  dtable <- dtable[dtable[["English_name"]] == specie,]
  dtable[dtable[["Year"]] != 2018,]
}
filter2 <- function(dtable, specie)
{
  dtable <- dtable[dtable[["English_name"]] == specie,]
}
#Generate histogram of all species based on filter.
#generate_histograms(dtable, "Year", ALL_SPECIES, filter1, 1983:2017, c(0,60), paste(BASE, "histograms\\", sep=""))
#generate_histograms(dtable, "Hour", ALL_SPECIES, filter2, 0:24, c(0,100), paste(BASE, "histograms3\\", sep=""))

#Generate histogramm of the vocalization types
vocal_freq <- table(dtable[["Vocalization_type"]])[c(3, 6, 1, 4, 2, 5)]
barplot(vocal_freq, col=VOCALIZATION_COLORS[vocal_freq], main="Histogram of Vocalization Typ)e", ylab="Frequency", xlab="Vocalization Type")

#hour      <- as.numeric(dtable[["Hour"]])
#frequency <- table(dtable[["Year"]], dtable[["Time"]])
#hist(hour, breaks=seq(0,23,l=25), main="Histogram of Hour of Day", xlab="Month", col="lightblue")
#hist3D(z=frequency, ybreaks=seq(0,23,l=25), xbreaks=seq(1983, 2018, l=36), border="Black", main="Histogram of Hour of Day", xlab="Year", ylab="Hour", zlab="Frequency")
#image2D(z=frequency, ybreaks=seq(0,23,l=25), border="Black", main="Histogram of Hour of Day", xlab="Year", ylab="Hour")
