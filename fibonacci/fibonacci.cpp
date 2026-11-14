#include <iostream>
#include <map>
#include <stdexcept>
#include <typeinfo>


std::map<int,long long> hist = {{0,0},{1,1}};

long long fibo (int x){

if (typeid(x) != typeid(int)) {
        throw std::invalid_argument("x must be an integer\n");
};

if (x<0){
throw std::invalid_argument("x must be positive");
};

if (hist.count(x)){
return hist[x];
};

hist[x] = fibo(x-1) + fibo(x-2);
return hist[x];
};



int main() {
    std::cout << fibo(50) << "\n";  
}
