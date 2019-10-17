using System;

namespace ProgramStructure
{
    /*
        Here I want to design a Stack taking
        advantage of the object type to make the
        Stack to store all kind of data types.
        This is the skeleton that I can write first
        besides the implementation. 

        - Which operations I need to implement in my Stack?
        - How a Stack works? See the related notes in datastructures.
        - How to implement a Stack. There are many ways to implement a stack.
        In this implementation of the stack the top element holds the instance
        of the next element. So when the top wants to pop, the instance of the
        next element take the place of top overriding the memory with the next
        element and the top is returned.
     */
    public class Stack
    {
        Entry top;
        public void Push(object data)
        {
            top = new Entry(top, data);
        }

        public object Pop()
        {
            if (top == null)
            {
                throw new InvalidOperationException();
            }

            object result = top.data;
            top = top.next;

            return result;
        }

        class Entry 
        {
            public Entry next;
            public object data;

            public Entry(Entry next, object data)
            {
                this.next = next;
                this.data = data;
            }
        }
    }
}
