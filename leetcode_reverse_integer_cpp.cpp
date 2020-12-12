class Solution {
public:
    int reverse(int x) {

       long long int newnum = 0;
        if (x > 2147483647 || x < -2147483648)
        {
            return 0;
        }
        while(x!=0)
        {
            newnum = newnum*10 + x%10;
            x=x/10;
            //cout<<newnum<<endl;
        }
        if ( newnum > 2147483647 || newnum < -2147483648)
        {
            return 0;
        }
        return newnum;
    }
};
