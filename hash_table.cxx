// C++ program to implement hashing with chaining 

#include<bits/stdc++.h> 
#include<iostream>
#include<cstdlib>
#include<string>
#include<cstdio>

using namespace std; 
  
class Hash 
{ 
        int BUCKET;                             // No. of buckets 
        list<int> *table;                       // Pointer to an list containing buckets 

        public: 
                Hash(int V);                    // Constructor 
  
                void insertItem(int x);         // inserts a key into hash table
                void deleteItem(int key);       // deletes a key from hash table 
                int hashFunction(int x)         // hash function to map values to key 
                { 
                        return (x % BUCKET); 
                } 
                void displayHash();           
}; 
  
Hash::Hash(int b) 
{ 
        this->BUCKET = b;                       // assign value to bucket 
        table = new list<int>[BUCKET];          // Add new list at bucket value
} 
  
void Hash::insertItem(int key) 
{ 
        int index = hashFunction(key);          // Use hash function to get the correct index  
        table[index].push_back(key);            // insert key onto the back of list
} 
  
void Hash::deleteItem(int key) 
{ 
        int index = hashFunction(key);          // get the hash index of key 
   
        list <int> :: iterator i;               // iterate through the list until the key is found.(iterator is part of the stl) 
        for (i = table[index].begin();i != table[index].end(); i++) 
        { 
                if (*i == key) 
                break;                          // Stop once found
        } 
  
        if (i != table[index].end()) 
                table[index].erase(i);          // if we are not at the end of the table, then we assume that we are on the found i♦
} 
  
// function to display hash table 
void Hash::displayHash() 
{ 
        for (int i = 0; i < BUCKET; i++) 
        { 
                cout << i; 
                for (auto x : table[i]) 
                        cout << " --> " << x; 
                cout << endl; 
        } 
} 
    
// Driver program  
int main() 
{ 
    Hash hash_table(7);                                      // 7 is count of buckets in hash table 
    int c,v;
    while (1) 
    {
        cout<<"1.Insert element into the table"<<endl;
        cout<<"2.Display elements from the table"<<endl;
        cout<<"3.Delete element at a key"<<endl;
        cout<<"4.Exit"<<endl;
        cout<<"Enter your choice: ";
        cin>>c;
        switch(c) 
        {
            case 1:
                cout<<"Enter a number to be inserted: ";
                cin>>v;
                hash_table.insertItem(v);
            break;
            case 2:
                hash_table.displayHash();
            break;
            case 3:
                cout<<"Enter the number to be deleted from the table: ";
                cin>>v;
                hash_table.deleteItem(v);
            break;
            case 4:
                exit(1);
            default:
                cout<<"\nEnter correct option\n";
        }
    }
    return 0; 
}
