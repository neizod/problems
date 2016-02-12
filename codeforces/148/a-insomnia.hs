import Data.List (nub)

zipList ls = header ls : (zipList . tailer) ls
    where header = foldr (\(h:_) a -> h:a) []
          tailer = foldr (\(_:t) a -> t:a) []

main = do
    rawData <- sequence $ replicate 5 getLine
    let [_, k, l, m, n, d] = 0 : map read rawData
        dragons = [cycle [i == j | i <- [1..j]] | j <- nub [k, l, m, n]]
    print $ length $ filter id $ map or $ take d $ zipList dragons
