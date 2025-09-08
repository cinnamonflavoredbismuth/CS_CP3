capacity += 5;
            int* temp = new int[capacity];
            for (int i = 0; i < entries; i++)
                temp[i] = goop[i];
            delete[] goop;
            goop = temp;