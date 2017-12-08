#lang racket

(define (false-as-one bool) (if bool 0 1))
(define (neq-as-one a b) (false-as-one (equal? a b)))

(define (zip ls rs)
  (cond [(null? ls) null]
        [(null? rs) null]
        [else (cons (cons (car ls) (car rs))
                    (zip (cdr ls) (cdr rs)))]))

(define (flip raw-pancakes)
  (letrec ([pancakes (string-append raw-pancakes "+")]
           [body (string->list pancakes)]
           [tail (cdr body)]
           [aux (lambda (pairs)
                  (if (null? pairs)
                    0
                    (+ (neq-as-one (car (car pairs)) (cdr (car pairs)))
                       (aux (cdr pairs)))))])
    (aux (zip body tail))))

(define (main)
  (let ([total-cases (string->number (read-line))])
    (for ([case-no total-cases])
      (let ([pancakes (read-line)])
        (printf "Case #~a: ~a\n"
                (add1 case-no)
                (flip pancakes))))))

(main)
