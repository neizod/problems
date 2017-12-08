import Text.Printf
import Data.List.Split (splitOn)


getInts :: IO [Int]
getInts = do
    it <- getLine
    return $ [read n | n <- splitOn " " it]


printList :: [Int] -> IO ()
printList [] = do printf "\n"
printList (g:gs) = do
    printf " %i" g
    printList gs


geometricSeries :: Int -> Int -> Int
geometricSeries 1    _      = 1
geometricSeries base power = quot (base^power - 1) (base - 1)


goldLocations :: Int -> Int -> [Int]
goldLocations pattern complexity =
    let basePosition = geometricSeries pattern complexity
    in  [placement * basePosition + 1 | placement <- [0..pattern-1]]


test :: Int -> IO ()
test t = do
    [pattern,complexity,_] <- getInts
    printf "Case #%i:" t
    printList $ goldLocations pattern complexity


main :: IO ()
main = do
    [loop] <- getInts
    sequence_ [test t | t <- [1..loop]]
