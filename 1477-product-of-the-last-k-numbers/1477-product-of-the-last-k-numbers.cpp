int prod[40000];
class ProductOfNumbers {
public:
    int z=0, i = 1;
    ProductOfNumbers() {
        prod[0] = 1;
    }
    
    void add(int num) {
        if(num==0){
            z =1;
            prod[i] = 1;
        }
        else{
            prod[i] = prod[i-1]*num;
            if(z>=1) z++;
        }
        cout<<prod[i]<<" ";
        i++;
    }
    
    int getProduct(int k) {
        if(k>=z && z!=0) return 0;
        // if(k==i-1) prod[i-1];
        return prod[i-1]/prod[i-k-1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */