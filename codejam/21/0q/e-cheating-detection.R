#!/usr/bin/env Rscript


neighbor_mean <- function(xs, n=5) {
    padxs <- c(0, cumsum(c(tail(xs, n%/%2), xs, head(xs, n%/%2))))
    (tail(padxs, -n) - head(padxs, -n)) / n
}


neighbor_median <- function(xs, n=5) {
    padxs <- c(tail(xs, n%/%2), xs, head(xs, n%/%2))
    apply(embed(padxs, n), 1, median)
}


partition_sd <- function(xs, ngroup=10) {
    apply(xs, 2, function(score) sd(colSums(matrix(score, ncol=ngroup))))
}


find_cheater <- function(scores) {
    colnames(scores) <- 1:100
    scores <- scores[order(rowSums(scores)),order(colSums(scores))]
    sd_scores <- partition_sd(scores)
    mu_scores <- neighbor_median(sd_scores)     # neighbor_mean also work
    suspect <- abs(sd_scores - mu_scores)
    colnames(scores)[which(suspect == max(suspect))]
}


if (!interactive()) {
    f <- file("stdin", "r")
    cases <- as.integer(readLines(f, n=1))
    percent <- as.integer(readLines(f, n=1))
    for (case in 1:cases) {
        raw <- readLines(f, n=100)
        input <- na.omit(as.integer(unlist(strsplit(raw, ""))))
        answer <- find_cheater(matrix(input, ncol=100))
        cat(paste0("Case #", case, ": ", answer, "\n"))
    }
}
