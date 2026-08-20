#Q1
k <- c(1, 2, 3, 4, 5)
sse <- c(600, 350, 220, 200, 190)
data.frame(K = k, SSE = sse)
plot(k, sse,type = "b",xlab = "Number of Clusters (K)",ylab = "SSE",main = "Elbow Method")
optimal_k <- 3
cat("Optimal Number of Clusters =", optimal_k)