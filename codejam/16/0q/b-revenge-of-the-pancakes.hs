import Text.Printf

getInt :: IO Int
getInt = do
    it <- getLine
    return $ read it


getPancakes :: IO String
getPancakes = do
    it <- getLine
    return $ it ++ "+"


countFlip :: String -> Int
countFlip pancakes = sum [neqOne a b | (a,b) <- zip pancakes (tail pancakes)]
    where neqOne a b = if a /= b then 1 else 0


test :: Int -> IO ()
test t = do
    pancakes <- getPancakes
    printf "Case #%i: %i\n" t $ countFlip pancakes


main :: IO ()
main = do
    loop <- getInt
    sequence_ [test t | t <- [1..loop]]
