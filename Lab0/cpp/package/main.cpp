#include <iostream>
#include <fstream>
#include <list>
#include <stdlib.h>

using namespace std;

int main()
{
    list<short> packages = {};
    list<short> expack = {};
    string buf;
    bool trigger = false;
    ifstream MyFile("..\\cpp\\data.txt");
    while (getline(MyFile, buf))    //main cycle
    {
        expack.clear();
        cout << buf << endl;
        packages.push_front(atoi(buf.c_str()));
        short min = packages.back();
        short max = packages.back();
        for (short n : packages)    //find Min and Max cycle
        {
            if (n>max)
                max = n;
            if (n<min)
                min = n;
        }
        for (short i = min+1; i < max; i++)     //
        {
            for (short j : packages)    //include check cycle
                if (i==j)
                {
                    trigger = true;
                    break;
                }
                else
                {
                    trigger = false;
                }
            if (trigger==false)
            {
                for (short k : expack)      //exclude check cycle
                {
                    if (i==k)
                    {
                        trigger = true;
                        break;
                    }
                    else
                    {
                        trigger = false;
                    }
                }
                if (trigger==false)
                    expack.push_back(i);
            }
        }
        if (!expack.empty())
        {
            cout << "Message " << min << "-" << max << " doesn't contain next packages: ";
            for (short n : expack)
                cout << n << " ";
            cout << endl;
        }
        else
        {
            cout << "Message " << min << "-" << max << "has been recieved!" << endl;
        }
    }
    MyFile.close();
    packages.clear();
    return 0;
}
