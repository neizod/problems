import Data.List.Split

least (0,y,z) = minimum [y,z]
least (x,y,0) = minimum [x,y]
least (x,y,z) = minimum [x,y,z]

scanEarth s [] = minimum s
scanEarth [] r = scanEarth (head r) (tail r)
scanEarth s r = do
    let p = [least each | each <- zip3 ([0] ++ init s) s (tail s ++ [0])]
        c = [fst x + snd x | x <- zip p (head r)]
    scanEarth c (tail r)


test_case = do
    rawSize <- getLine
    let rows = head [read x + 0 | x <- splitOn " " rawSize]
    rawEarth <- sequence [getLine | _ <- [1..rows]]
    let earth = [[read x + 0 | x <- splitOn " " l, x /= "\r"] | l <- rawEarth]
    print (scanEarth [] earth)

main = do
    n <- getLine
    sequence_ [test_case | _ <- [1..read n]]
