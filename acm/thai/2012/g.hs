import Data.List
import Data.List.Split

fridge f = (head sf):(map (\ x -> x - 1) (tail sf)) where sf = sort f

storeFood d f = do
    if all (> 0) f
        then storeFood (d+1) (fridge f)
        else d


test_case = do
    getLine
    foods <- getLine
    let output = storeFood 0 [read x + 0 | x <- splitOn " " foods, x /= ""]
    print output

main = do
    n <- getLine
    sequence_ [test_case | _ <- [1..read n]]
