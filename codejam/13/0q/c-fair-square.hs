import Data.List.Split (splitOn)

boolAsNum b = if b then 1 else 0

isSquare x = r^2 == x
    where r = sqrt x

isPalindrome x = s == reverse s
    where s = show x

countFair x y
    | x > y     = 0
    | otherwise = (boolAsNum $ all isPalindrome [x,x^2]) + countFair (x+1) y

eachLoop nosLoop = do
    raw <- getLine
    let rawSqrtNum = [sqrt $ read x | x <- splitOn " " raw]
        [start, stop] = [f x | (f,x) <- zip [ceiling, floor] rawSqrtNum]
    putStrLn $ "Case #" ++ (show nosLoop) ++ ": " ++ (show $ countFair start stop)

main = do
    allLoop <- getLine
    sequence_ [eachLoop n | n <- [1..read allLoop]]
