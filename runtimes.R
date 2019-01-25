# load data
myData <- read.table("~/Documents/winterY1/algorithms/homeworks/homework1/example/runtimes.txt")
colnames(myData) <- c("inputSize", "trial", "alg", "n_assignments", "n_conditionals")
myData$n_operations <- myData$n_assignments + myData$n_conditionals


# stats
myData$squared_input <- myData$inputSize**2
summary(lm(n_operations~squared_input, data=subset(myData, alg=="bubblesort_core")))
fit_x = seq(100, 1000, 100)
bubbleF <- function(x) x**2 * 0.998
myData$nlogn_input <- myData$inputSize*log2(myData$inputSize)
summary(lm(n_operations~nlogn_input, data=subset(myData, alg=="quicksort_core")))
quickF <- function(x) x*log2(x) * 4.493 - 300

bubbleData <- subset(myData, alg=="bubblesort_core")
plot(bubbleData$inputSize, bubbleData$n_operations)
points(fit_x, bubble_y)

# plot
library(ggplot2)
myData$inputSize <- factor(myData$inputSize)
ggplot(myData, aes(x=inputSize, y=n_operations, colour=alg)) + geom_point() + labs(x="number of elements to sort", y = "number of operations (assignments + conditionals)", title = "runtime of quicksort and bubble sort", colour="algorithm") + stat_function(fun=bubbleF, color="red") + stat_function(fun=quickF, color="deepskyblue")

myBubbleFit <- as.data.frame(fit_x, bubble_y)
