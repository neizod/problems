import Text.Printf
import Data.List.Split (splitOn)

cookieTime c f x =
    let aux t ic c f x = if ww > uw then aux (t+nf) ec c f x else t+ww
            where nf = c / ic
                  ec = f + ic
                  ww = x / ic
                  uw = x / ec + nf
    in  aux 0 2.0 c f x

eachLoop nosLoop = do
    raw <- getLine
    let [c, f, x] = [read x :: Double | x <- splitOn " " raw]
        answer = cookieTime c f x
    printf "Case #%d: %.7f\n" nosLoop answer

main = do
    allLoop <- getLine
    sequence_ [eachLoop n | n <- [1..read allLoop :: Integer]]
