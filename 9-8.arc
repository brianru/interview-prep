(def mk_change0 (amt cns)
  (if (<= amt 0) 0 ; guard against bad input
    (letf f (a c) (if (is a 0) 1
                      (or empty.c (< a 0)) 0 
                    (+ (f (- a car.c) c)
                       (f a cdr.c)))
      (f amt cns))))

(def mk_change (amt cns (o print? nil))
  (if (<= amt 0) 0
    (letf f (a c ch) (if (is a 0) (do1 1 (and print? (prn rev.ch)))
                         (or empty.c (< a 0)) 0
                       (+ (f (- a car.c) c (cons car.c ch))
                          (f a cdr.c ch)))
      (f amt cns nil))))
