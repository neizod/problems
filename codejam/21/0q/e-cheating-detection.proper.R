#!/usr/bin/env Rscript

cumsig <- function(x) log(exp(x)+1)


sumsig <- function(a, b) (cumsig(b)-cumsig(a))/(b-a)


guess <- function(p, k=3, b=exp(-2*k)) k+log((1-b)/(1-b^(1-p))-1)


expect_dist <- function(skill, k=3, bins=10) {
    endpoints <- seq(skill-k, skill+k, length=bins+1)
    sumsig(head(endpoints, -1), tail(endpoints, -1))
}


discrepancy <- function(score, bins=10) {
    theory <- expect_dist(guess(sum(score)/10000), bins=bins)
    actual <- colSums(matrix(score, ncol=bins))*(bins/10000)
    abs(sd(theory)-sd(actual))
}


find_cheater <- function(scores) {
    tt <- guess(colSums(scores)/10000)
    if (max(tt) > 3) return(which(tt == max(tt)))
    suspects <- apply(scores[order(rowSums(scores)),], 2, discrepancy)
    which(suspects == max(suspects))
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
