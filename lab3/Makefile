fibonacci: main.o fibonacci.o
	cc main.o fibonacci.o -o fibonacci

main.o: main.c headers/fibonacci.h
	cc -Iheaders -c main.c -o main.o

fibonacci.o: fibonacci.c headers/fibonacci.h
	cc -Iheaders -c fibonacci.c -o fibonacci.o

run: fibonacci
	./fibonacci

clean:
	rm -f main.o fibonacci.o fibonacci
