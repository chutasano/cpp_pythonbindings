# location of the Python header files
 
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
 
# location of the Boost Python include files and library
 
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib/x86_64-linux-gnu
 
test.so: test.o
	g++ test.o -shared -Wl,--export-dynamic -L$(BOOST_LIB) -lboost_python-py27 -lboost_thread -lboost_chrono -L/usr/lib/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o test.so

test.o: test.cpp
	g++ -c -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC test.cpp

clean:
	rm test.o test.so
