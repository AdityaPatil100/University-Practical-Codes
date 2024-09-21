#include <iostream>
#include <string.h>
using namespace std;

class node
{
public:
    string keyword;
    string meaning;
    node *right;
    node *left;
    node(string keyword, string meaning)
    {
        this->keyword = keyword;
        this->meaning = meaning;
        this->left = NULL;
        this->right = NULL;
    }
};

class Dictionary
{
public:
    node *root = NULL;

    node *insertNode(node *root, string keyword, string meaning)
    {
        if (root == NULL)
        {
            return new node(keyword, meaning);
        }
        if (keyword < root->keyword)
        {
            root->left = insertNode(root->left, keyword, meaning);
        }
        else if (keyword > root->keyword)
        {
            root->right = insertNode(root->right, keyword, meaning);
        }
        return root;
    }

    void ascending(node *root)
    {
        if (!root)
        {
            return;
        }
        else
        {
            ascending(root->left);
            cout << "Keyword: ";
            cout << root->keyword << endl;
            cout << "Meaning: ";
            cout << root->meaning << endl;
            cout << endl;
            ascending(root->right);
        }
    }
    void descending(node *root)
    {
        if (!root)
        {
            return;
        }
        else
        {
            descending(root->right);
            cout << "Keyword: ";
            cout << root->keyword << endl;
            cout << "Meaning: ";
            cout << root->meaning << endl;
            cout << endl;
            descending(root->left);
        }
    }

    void countComparisions(string keyword)
    {
        int count = 0;
        node *current = this->root;
        while (current != NULL)
        {
            if (current->keyword == keyword)
            {
                count++;
                break;
            }
            else if (keyword < current->keyword)
            {
                current = current->left;
                count++;
            }
            else if (keyword > current->keyword)
            {
                current = current->right;
                count++;
            }
        }
        cout << "The no. of comparisions to find " << keyword << " is " << count << endl;
    }

    void updateEntry(string keyword, string meaning)
    {
        node *current = this->root;
        while (current != NULL)
        {
            if (current->keyword == keyword)
            {
                current->keyword = keyword;
                current->meaning = meaning;
                break;
            }
            else if (keyword < current->keyword)
            {
                current = current->left;
            }
            else if (keyword > current->keyword)
            {
                current = current->right;
            }
        }
        cout << "Dictionary after updating: " << endl;
        ascending(this->root);
    }

    node *preorderSucc(node *root)
    {
        while (root->left != NULL)
        {
            root = root->left;
        }
        return root;
    }
    node *deleteEntry(node *root, string keyword)
    {

        if (keyword < root->keyword)
        {
            root->left = deleteEntry(root->left, keyword);
        }
        else if (keyword > root->keyword)
        {
            root->right = deleteEntry(root->right, keyword);
        }
        else
        {
            if (root->left == NULL)
            {
                node *temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == NULL)
            {
                node *temp = root->left;
                delete root;
                return temp;
            }
            else
            {
                node *temp = preorderSucc(root->right);
                root->keyword = temp->keyword;
                root->meaning = temp->meaning;
                root->right = deleteEntry(root->right, temp->keyword);
            }
        }
        return root;
    }
};

int main()
{
    Dictionary D;
    string keyword;
    string meaning;
    char cont = 'y';
    do
    {
        cout << "<-------------Menu------------->" << endl;
        cout << "1. Insert a new Entry" << endl;
        cout << "2. Display the Dictionary in Ascending Order" << endl;
        cout << "3. Display the Dictionary in Descending Order" << endl;
        cout << "4. Delete keyword" << endl;
        cout << "5. Get the no's of comparisons" << endl;
        cout << "6. Update an Entry" << endl;
        cout << "Enter a choice: ";
        int choice;
        cin >> choice;
        switch (choice)
        {
        case 1:
            int n;
            cout << "Please enter the no. of entries: ";
            cin >> n;
            for (int i = 0; i < n; i++)
            {
                cout << "Enter the keyword: ";
                cin >> keyword;
                cout << "Enter the meaning: ";
                cin >> meaning;
                D.root = D.insertNode(D.root, keyword, meaning);
            }
            cout << "Keywords Entered Successfully!" << endl;
            break;
        case 2:
            D.ascending(D.root);
            break;
        case 3:
            D.descending(D.root);
            break;
        case 4:
            cout << "Enter the keyword to be deleted: ";
            cin >> keyword;
            D.root = D.deleteEntry(D.root, keyword);
            cout << "Keyword Deleted Successfully!" << endl;
            cout << "Dictionary after deletion: " << endl;
            D.ascending(D.root);
            break;
        case 5:
            cout << "Enter the word to be searched: ";
            cin >> keyword;
            D.countComparisions(keyword);
            break;
        case 6:
            cout << "Enter the keyword to be updated: ";
            cin >> keyword;
            cout << "Enter the updated meaning: ";
            cin >> meaning;
            D.updateEntry(keyword, meaning);
            break;
        default:
            cout << "Invalid Choice!" << endl;
            break;
        }
        cout << "Do you want to continue? (y/n): ";
        cin >> cont;

    } while (cont == 'y');
    cout << "Program Ended Successfully!" << endl;
    return 0;
}

