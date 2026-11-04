fibonacci: main.o fibonacci.o
	cc main.o fibonacci.o -o fibonacci

fibonacci_test: fibonacci.o tests.o
	cc fibonacci.o tests.o -o fibonacci_test

tests.o: tests.c headers/fibonacci.h
	cc -Iheaders -c tests.c -o tests.o

main.o: main.c headers/fibonacci.h
	cc -Iheaders -c main.c -o main.o

fibonacci.o: fibonacci.c headers/fibonacci.h
	cc -Iheaders -c fibonacci.c -o fibonacci.o

run: fibonacci
	./fibonacci

test: fibonacci_test
	./fibonacci_test

clean:
	rm -f main.o fibonacci.o fibonacci fibonacci_test
