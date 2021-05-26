import Text.Printf


triangularNumber :: Int -> Int
triangularNumber n = n*(n+1) `div` 2


findOrder :: Int -> Int -> [Int]
findOrder 1 c = [0]
findOrder n c = k : findOrder (n-1) (c-k)
    where k = min n (c-(n-2))


getSample :: [Int] -> [Int] -> [Int]
getSample [] out     = out
getSample (x:xs) out = getSample xs $ (reverse (take x zs)) ++ (drop x zs)
    where zs = (1 + length xs) : out


findReversort :: Int -> Int -> Maybe [Int]
findReversort n c = if c < n-1 || c > (triangularNumber n)-1
    then Nothing
    else Just $ getSample (reverse (findOrder n c)) []


test :: Int -> IO ()
test t = do
    [n,c] <- getInts
    let answer = case findReversort n c of
                      Nothing -> "IMPOSSIBLE"
                      Just xs -> unwords (map show xs)
    printf "Case #%d: %s\n" t answer


getInts :: IO [Int]
getInts = do
    xs <- getLine
    return [read x | x <- words xs]


getInt :: IO Int
getInt = do
    x <- getLine
    return $ read x


main :: IO ()
main = do
    loop <- getInt
    sequence_ [test t | t <- [1..loop]]
