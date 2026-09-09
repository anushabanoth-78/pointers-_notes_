<section>
  <h2>1. Memory Address</h2>

  <p>When we create a variable, it occupies a location in computer memory.</p>

  <p><strong>Example:</strong></p>

  <pre><code>int a = 10;</code></pre>

  <p><strong>Conceptually:</strong></p>

  <table>
    <tr>
      <th>Variable</th>
      <th>Value</th>
      <th>Address</th>
    </tr>
    <tr>
      <td>a</td>
      <td>10</td>
      <td>100</td>
    </tr>
  </table>

  <p>Here:</p>

  <ul>
    <li><code>10</code> → value of <code>a</code></li>
    <li><code>100</code> → memory address of <code>a</code></li>
  </ul>

  <p>
    The actual address will normally look like a hexadecimal number, for example:
  </p>

  <pre><code>0x7ffe1234</code></pre>

  <p>
    The address-of operator <code>&amp;</code> gives the address of a variable.
  </p>

  <pre><code>cout &lt;&lt; &amp;a;</code></pre>
</section>
<section>
  <h2>2. What is a Pointer?</h2>

  <h3>Definition</h3>

  <blockquote>
    <strong>A pointer is a variable that stores the memory address of another variable.</strong>
  </blockquote>

  <p><strong>Example:</strong></p>

  <pre><code>int a = 10;
int *ptr = &amp;a;</code></pre>

  <p><strong>Think of it like this:</strong></p>

  <pre><code>a
+---------+
|   10    |
+---------+
 Address = 100
     ↑
     |
+---------+
|   100   |
+---------+
   ptr</code></pre>

  <p>So:</p>

  <pre><code>a       → value = 10
&amp;a      → address of a = 100
ptr     → contains address 100</code></pre>

  <p>Therefore:</p>

  <pre><code>ptr == &amp;a</code></pre>

  <p>
    conceptually means both represent the same address.
  </p>

  <p>
    The pointer itself is also a variable, so
    <strong>the pointer has its own memory address</strong>,
    which is different from the address stored inside it.
  </p>
</section><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>C++ Pointers — Complete Study Notes</title>
</head>
<body>

<h1>3. Pointer Syntax</h1>

<p>For an integer pointer:</p>

<pre><code>int *ptr;</code></pre>

<p>For a float pointer:</p>

<pre><code>float *ptr;</code></pre>

<p>For a character pointer:</p>

<pre><code>char *ptr;</code></pre>

<p>General form:</p>

<pre><code>data_type *pointer_name;</code></pre>

<p>Example:</p>

<pre><code>int a = 10;
int *ptr = &amp;a;</code></pre>

<p>Here <code>ptr</code> is an <strong>integer pointer</strong>, because it points to an <code>int</code> variable.</p>

<hr>

<h1>4. <code>&amp;</code> Address-of Operator</h1>

<p>The symbol <code>&amp;</code> has multiple uses in C++.</p>

<p>For pointers, the important use is:</p>

<pre><code>&amp;a</code></pre>

<p>means:</p>

<blockquote><strong>Give me the address of <code>a</code>.</strong></blockquote>

<p>Example:</p>

<pre><code>int a = 10;

cout &lt;&lt; &amp;a;</code></pre>

<p>Output will be some hexadecimal memory address.</p>

<p>Important:</p>

<pre><code>a</code></pre>

<p>means <strong>value of a</strong></p>

<pre><code>&amp;a</code></pre>

<p>means <strong>address of a</strong></p>

<hr>

<h1>5. <code>*</code> Dereference Operator</h1>

<p>The <code>*</code> operator also has multiple uses.</p>

<p>In:</p>

<pre><code>int *ptr;</code></pre>

<p><code>*</code> is used to declare a pointer.</p>

<p>But when we write:</p>

<pre><code>*ptr</code></pre>

<p>it means <strong>dereference the pointer</strong>.</p>

<h3>Definition</h3>

<blockquote>
  <strong>Dereferencing means accessing the value stored at the memory address held by the pointer.</strong>
</blockquote>

<p>Example:</p>

<pre><code>int a = 10;
int *ptr = &amp;a;

cout &lt;&lt; *ptr;</code></pre>

<p>Output:</p>

<pre><code>10</code></pre>

<p>Why?</p>

<pre><code>ptr
 ↓
100
 ↓
address 100 contains 10</code></pre>

<p>Therefore:</p>

<pre><code>*ptr</code></pre>

<p>gives:</p>

<pre><code>10</code></pre>

<p>Both <code>*(&amp;a)</code> and <code>*ptr</code> give the value <code>10</code>.</p>

<hr>

<h1>6. The Most Important Difference</h1>

<table border="1">
  <tr>
    <th>Expression</th>
    <th>Meaning</th>
  </tr>
  <tr>
    <td><code>a</code></td>
    <td>Value of <code>a</code></td>
  </tr>
  <tr>
    <td><code>&amp;a</code></td>
    <td>Address of <code>a</code></td>
  </tr>
  <tr>
    <td><code>ptr</code></td>
    <td>Address stored inside <code>ptr</code></td>
  </tr>
  <tr>
    <td><code>*ptr</code></td>
    <td>Value at the address stored in <code>ptr</code></td>
  </tr>
  <tr>
    <td><code>&amp;ptr</code></td>
    <td>Address of the pointer itself</td>
  </tr>
</table>

<p>Example:</p>

<pre><code>int a = 10;
int *ptr = &amp;a;</code></pre>

<p>Conceptually:</p>

<pre><code>a = 10

&amp;a = 100

ptr = 100

*ptr = 10

&amp;ptr = 300   ← pointer's own address</code></pre>

<p>This distinction is <strong>extremely important for interviews and MCQs</strong>.</p>

<hr>

<h1>7. Pointer to Pointer</h1>

<p>A pointer can store the address of another pointer.</p>

<p>This is called a:</p>

<blockquote><strong>Pointer to Pointer</strong></blockquote>

<p>Syntax:</p>

<pre><code>int **ptr2;</code></pre>

<p>Example:</p>

<pre><code>int a = 10;

int *ptr = &amp;a;

int **ptr2 = &amp;ptr;</code></pre>

<p>Think:</p>

<pre><code>a
Address = 100
Value = 10
      ↑
      |
ptr
Address = 300
Value = 100
      ↑
      |
ptr2
Address = 500
Value = 300</code></pre>

<p>Therefore:</p>

<pre><code>ptr2 → address of ptr
ptr  → address of a
a    → actual value</code></pre>

<p><code>int*</code> points to an <code>int</code>, while <code>int**</code> points to an <code>int*</code>.</p>

<hr>

<h1>8. Dereferencing Pointer to Pointer</h1>

<p>Suppose:</p>

<pre><code>int a = 10;
int *ptr = &amp;a;
int **ptr2 = &amp;ptr;</code></pre>

<h3><code>ptr</code></h3>

<pre><code>100</code></pre>

<h3><code>*ptr</code></h3>

<pre><code>10</code></pre>

<h3><code>ptr2</code></h3>

<pre><code>address of ptr</code></pre>

<h3><code>*ptr2</code></h3>

<p>This gives:</p>

<pre><code>ptr</code></pre>

<p>which contains:</p>

<pre><code>100</code></pre>

<h3><code>**ptr2</code></h3>

<p>First dereference:</p>

<pre><code>*ptr2 → ptr → 100</code></pre>

<p>Second dereference:</p>

<pre><code>**ptr2 → value at address 100 → 10</code></pre>

<p>So:</p>

<pre><code>cout &lt;&lt; **ptr2;</code></pre>

<p>prints:</p>

<pre><code>10</code></pre>

<p>This is one of the most important pointer-to-pointer concepts.</p>

<hr>

<h1>9. NULL Pointer</h1>

<p>A <strong>NULL pointer</strong> is a pointer that does not point to a valid memory location.</p>

<p>Example:</p>

<pre><code>int *ptr = NULL;</code></pre>

<p>It means:</p>

<pre><code>ptr → no valid memory location</code></pre>

<p>A null pointer can be used to indicate that no memory address has been assigned yet.</p>

<h3>Why use NULL?</h3>

<p>Consider:</p>

<pre><code>int *ptr;</code></pre>

<p>If you don't initialize it, it may contain an indeterminate/garbage value.</p>

<p>Instead:</p>

<pre><code>int *ptr = NULL;</code></pre>

<p>clearly indicates that the pointer isn't currently pointing to a valid object.</p>

<h3>Important</h3>

<p>Do <strong>not</strong> dereference a null pointer:</p>

<pre><code>cout &lt;&lt; *ptr;</code></pre>

<p>This is invalid because <code>ptr</code> doesn't point to a valid object.</p>

<p>It can lead to a runtime error such as a <strong>segmentation fault</strong>.</p>

<hr>

<h1>10. Pointer and Pass by Reference</h1>

<p>Pointers can be used to modify the original variable inside a function.</p>

<p>Example:</p>

<pre><code>void change(int *p) {
    *p = 20;
}

int main() {
    int a = 10;

    change(&amp;a);

    cout &lt;&lt; a;
}</code></pre>

<p>Output:</p>

<pre><code>20</code></pre>

<p>Why?</p>

<p>Initially:</p>

<pre><code>a = 10</code></pre>

<p>We pass:</p>

<pre><code>&amp;a</code></pre>

<p>The function receives the address.</p>

<p>Inside:</p>

<pre><code>*p = 20;</code></pre>

<p>means:</p>

<blockquote>
  Go to the address stored in <code>p</code> and change the value there to <code>20</code>.
</blockquote>

<p>Therefore the original <code>a</code> becomes <code>20</code>.</p>

<p>This is <strong>pass by reference using pointers</strong>.</p>

<hr>

<h1>11. Pass by Reference Using Alias / Reference</h1>

<p>C++ also provides references.</p>

<p>Example:</p>

<pre><code>void change(int &amp;b) {
    b = 20;
}</code></pre>

<p>Then:</p>

<pre><code>int a = 10;

change(a);

cout &lt;&lt; a;</code></pre>

<p>Output:</p>

<pre><code>20</code></pre>

<p>Here <code>b</code> is an <strong>alias</strong> for <code>a</code>.</p>

<p>That means:</p>

<pre><code>a and b
   ↓
same memory location</code></pre>

<p>So changing <code>b</code> changes <code>a</code>.</p>

<h3>Easy difference</h3>

<pre><code>int *p</code></pre>

<p>→ pointer</p>

<pre><code>int &amp;b</code></pre>

<p>→ reference/alias</p>

<hr>

<h1>12. Array and Pointer</h1>

<p>Suppose:</p>

<pre><code>int arr[] = {10, 20, 30, 40};</code></pre>

<p>The array elements are stored in contiguous memory.</p>

<p>Conceptually:</p>

<pre><code>Address       Value

100            10
104            20
108            30
112            40</code></pre>

<p>The array name <code>arr</code> behaves like a pointer to the first element in many expressions.</p>

<p>So:</p>

<pre><code>arr</code></pre>

<p>represents the address of the first element.</p>

<p>Therefore:</p>

<pre><code>*arr</code></pre>

<p>gives:</p>

<pre><code>10</code></pre>

<p>The array name points to the element at index <code>0</code>.</p>

<hr>

<h1>13. <code>arr + 1</code></h1>

<p>This is very important.</p>

<p>If:</p>

<pre><code>arr</code></pre>

<p>points to:</p>

<pre><code>100</code></pre>

<p>then:</p>

<pre><code>arr + 1</code></pre>

<p>does <strong>not necessarily mean address 101</strong>.</p>

<p>For an <code>int</code> array, if an <code>int</code> occupies 4 bytes:</p>

<pre><code>arr       → 100
arr + 1   → 104
arr + 2   → 108
arr + 3   → 112</code></pre>

<p>Therefore:</p>

<pre><code>*(arr + 1)</code></pre>

<p>gives:</p>

<pre><code>20</code></pre>

<p>and:</p>

<pre><code>*(arr + 2)</code></pre>

<p>gives:</p>

<pre><code>30</code></pre>

<p>This is because pointer arithmetic moves according to the size of the pointed-to type.</p>

<hr>

<h1>14. Array Indexing and Pointer Arithmetic</h1>

<p>These are equivalent:</p>

<pre><code>arr[0]</code></pre>

<p>and:</p>

<pre><code>*(arr + 0)</code></pre>

<p>Similarly:</p>

<pre><code>arr[1] == *(arr + 1)</code></pre>

<pre><code>arr[2] == *(arr + 2)</code></pre>

<pre><code>arr[3] == *(arr + 3)</code></pre>

<p>Example:</p>

<pre><code>int arr[] = {10, 20, 30, 40};

cout &lt;&lt; *(arr + 0);  // 10
cout &lt;&lt; *(arr + 1);  // 20
cout &lt;&lt; *(arr + 2);  // 30
cout &lt;&lt; *(arr + 3);  // 40</code></pre>

<hr>

<h1>15. Pointer Arithmetic</h1>

<h3>Definition</h3>

<blockquote>
  <strong>Pointer arithmetic is performing arithmetic operations on pointers to move between memory locations/elements.</strong>
</blockquote>

<p>Important operations include:</p>

<pre><code>p++
p--
p + n
p - n
p1 - p2
pointer comparisons</code></pre>

<hr>

<h1>16. <code>p++</code></h1>

<p>Suppose:</p>

<pre><code>int *p;</code></pre>

<p>and:</p>

<pre><code>p = 100</code></pre>

<p>If an <code>int</code> is 4 bytes:</p>

<pre><code>p++;</code></pre>

<p>makes:</p>

<pre><code>p = 104</code></pre>

<p>Not:</p>

<pre><code>p = 101</code></pre>

<p>Why?</p>

<p>Because pointer arithmetic is based on the size of the pointed-to type.</p>

<p>For an <code>int *</code>:</p>

<pre><code>+1 → +sizeof(int)</code></pre>

<p>If <code>sizeof(int) = 4</code>:</p>

<pre><code>+1 → +4 bytes</code></pre>

<hr>

<h1>17. <code>p--</code></h1>

<p>Similarly:</p>

<pre><code>p--;</code></pre>

<p>For an <code>int *</code>, this moves back by one <code>int</code>.</p>

<p>If:</p>

<pre><code>p = 100</code></pre>

<p>then:</p>

<pre><code>p-- → 96</code></pre>

<p>assuming <code>int</code> is 4 bytes.</p>

<p>So:</p>

<pre><code>p++ → next int
p-- → previous int</code></pre>

<hr>

<h1>18. <code>p + n</code></h1>

<p>Suppose:</p>

<pre><code>p = 100</code></pre>

<p>and <code>p</code> is an <code>int*</code>.</p>

<p>Then:</p>

<pre><code>p + 1</code></pre>

<p>moves one integer:</p>

<pre><code>100 + 4 = 104</code></pre>

<p><code>p + 2</code> moves two integers:</p>

<pre><code>100 + 8 = 108</code></pre>

<p><code>p + 3</code> moves three integers:</p>

<pre><code>100 + 12 = 112</code></pre>

<p>So remember:</p>

<pre><code>p + n</code></pre>

<p>means:</p>

<blockquote>
  Move <code>n</code> elements forward, according to the pointer's type.
</blockquote>

<hr>

<h1>19. Pointer Subtraction</h1>

<p>Two pointers can be subtracted <strong>when they point into the same array/object sequence and are of compatible type</strong>.</p>

<p>Example:</p>

<pre><code>p1 → 100
p2 → 108</code></pre>

<p>If they are <code>int*</code> and an <code>int</code> is 4 bytes:</p>

<pre><code>p2 - p1</code></pre>

<p>gives:</p>

<pre><code>2</code></pre>

<p>because there are two <code>int</code> elements between the positions.</p>

<p>It does <strong>not</strong> return <code>8</code> as the byte difference.</p>

<p>It returns the difference in <strong>elements</strong>.</p>

<hr>

<h1>20. Pointer Addition</h1>

<p>This is an important interview point:</p>

<pre><code>p1 + p2</code></pre>

<p>❌ Pointer + pointer is not allowed.</p>

<p>But:</p>

<pre><code>p + 1</code></pre>

<p>✅ Pointer + integer is allowed.</p>

<p>And:</p>

<pre><code>p1 - p2</code></pre>

<p>✅ Pointer subtraction is allowed when the pointers are appropriately related, such as pointing into the same array.</p>

<hr>

<h1>21. Comparing Pointers</h1>

<p>Pointers can also be compared.</p>

<p>For example:</p>

<pre><code>p1 &lt; p2</code></pre>

<pre><code>p1 == p2</code></pre>

<pre><code>p1 != p2</code></pre>

<p>For pointers into the same array, relational comparisons such as <code>&lt;</code> and <code>&gt;</code> indicate their relative positions.</p>

<hr>

<h1>22. Most Important Example</h1>

<p>Consider:</p>

<pre><code>int a = 5;

int *p = &amp;a;

int **q = &amp;p;</code></pre>

<p>Conceptually:</p>

<pre><code>a
Address = 100
Value = 5

      ↑
      |
p
Address = 500
Value = 100

      ↑
      |
q
Address = 700
Value = 500</code></pre>

<p>Now understand each:</p>

<h3><code>a</code></h3>

<pre><code>5</code></pre>

<h3><code>&amp;a</code></h3>

<pre><code>100</code></pre>

<h3><code>p</code></h3>

<pre><code>100</code></pre>

<h3><code>*p</code></h3>

<pre><code>5</code></pre>

<h3><code>q</code></h3>

<pre><code>500</code></pre>

<h3><code>*q</code></h3>

<pre><code>100</code></pre>

<h3><code>**q</code></h3>

<pre><code>5</code></pre>

<p>This single example is enough to understand the basic pointer chain.</p>

<hr>

<h1>23. The Golden Rule ⭐</h1>

<p>Whenever you see <code>*</code>, ask:</p>

<blockquote>
  <strong>Am I declaring a pointer, or am I dereferencing a pointer?</strong>
</blockquote>

<p>Example:</p>

<pre><code>int *p;</code></pre>

<p>Here <code>*</code> means:</p>

<blockquote><code>p</code> is a pointer to an integer.</blockquote>

<p>But:</p>

<pre><code>*p</code></pre>

<p>Here <code>*</code> means:</p>

<blockquote>
  Give me the value at the address stored in <code>p</code>.
</blockquote>

<hr>

<h1>24. The Golden Rule for <code>&amp;</code> ⭐</h1>

<p>When you see:</p>

<pre><code>&amp;a</code></pre>

<p>think:</p>

<blockquote><strong>Address of <code>a</code></strong></blockquote>

<p>But when you see:</p>

<pre><code>int &amp;b = a;</code></pre>

<p>the <code>&amp;</code> is being used for a <strong>reference/alias</strong>, not as the address-of operator.</p>

<hr>

<h1>25. One-Page Revision Sheet</h1>

<pre><code>POINTERS
│
├── Memory Address
│     └── Address of variable → &amp;a
│
├── Pointer
│     └── int *p = &amp;a
│
├── Dereference
│     └── *p → value at address
│
├── Pointer to Pointer
│     └── int **q = &amp;p
│
├── NULL Pointer
│     └── int *p = NULL
│
├── Pass by Reference
│     ├── Using pointer
│     └── Using reference/alias
│
├── Array Pointer
│     └── arr → first element
│
└── Pointer Arithmetic
      ├── p++
      ├── p--
      ├── p + n
      ├── p - n
      ├── p1 - p2
      └── pointer comparisons</code></pre>

<h2>⭐ Remember these 7 lines</h2>

<pre><code>int a = 10;

&amp;a       // address of a
int *p = &amp;a;

p        // address stored in p
*p       // value stored at that address

int **q = &amp;p;

*q       // p's stored address
**q      // a's actual value</code></pre>

<p>
  <strong>
    If you understand these lines properly, the rest of the pointer chapter becomes much easier.
  </strong>
</p>

<h1>How Many Types of Pointers?</h1>

<p>For your C++ study, learn these common pointer types:</p>

<ol>
  <li><strong>Null Pointer</strong> – points to nothing.</li>
  <li><strong>Void Pointer (<code>void*</code>)</strong> – can hold the address of different data types.</li>
  <li><strong>Wild Pointer</strong> – uninitialized pointer.</li>
  <li><strong>Dangling Pointer</strong> – points to memory that is no longer valid.</li>
  <li><strong>Pointer to Pointer (<code>int**</code>)</strong> – stores the address of another pointer.</li>
  <li><strong>Function Pointer</strong> – stores the address of a function.</li>
  <li><strong>Constant Pointer</strong> – the pointer itself cannot change its address.</li>
  <li><strong>Pointer to Constant</strong> – the value pointed to cannot be changed through the pointer.</li>
  <li><strong>Smart Pointers</strong> – C++ pointers such as <code>unique_ptr</code>, <code>shared_ptr</code>, and <code>weak_ptr</code>.</li>
</ol>

<h3>⭐ For your current pointer chapter</h3>

<p>
  <strong>
    Normal Pointer → Pointer to Pointer → Null Pointer → Array Pointer →
    Function Pointer → Dangling/Wild Pointers → Smart Pointers
  </strong>
</p>

<p>
  Don't confuse <strong>pointer types</strong> with <strong>pointer operations</strong>
  like <code>p++</code>, <code>p--</code>, <code>p+n</code>, and <code>p1-p2</code>.
  Those are operations, not separate pointer types.
</p>

<h1>C++ POINTERS — COMPLETE STUDY NOTES</h1>

<h2>1. What is a Pointer?</h2>

<h3>Definition</h3>

<p>
  A <strong>pointer</strong> is a special variable that stores the
  <strong>memory address of another variable</strong>.
</p>

<p>Example:</p>

<pre><code>int a = 10;
int *ptr = &amp;a;</code></pre>

<p>Here:</p>

<ul>
  <li><code>a</code> → normal variable</li>
  <li><code>&amp;a</code> → address of <code>a</code></li>
  <li><code>ptr</code> → pointer variable</li>
  <li><code>ptr</code> stores the address of <code>a</code></li>
  <li><code>*ptr</code> → value stored at that address</li>
</ul>

<h3>Easy way to remember</h3>

<pre><code>a = 10
     ↓
   Address
     ↓
    ptr</code></pre>

<p>Think:</p>

<blockquote>
  <strong>Pointer = variable that stores an address.</strong>
</blockquote>

<h2>2. Why Do We Need Pointers?</h2>

<p>
  Pointers are useful when we need to work with <strong>memory addresses</strong>
  and when we want one variable to access or modify another variable indirectly.
</p>

<p>They become particularly important for concepts such as:</p>

<ul>
  <li>Pass by reference</li>
  <li>Arrays</li>
  <li>Linked lists</li>
  <li>Trees</li>
  <li>Dynamic memory</li>
  <li>Data structures</li>
</ul>

<h2>3. Address-of Operator <code>&amp;</code></h2>

<p>
  The <code>&amp;</code> operator can be used to obtain the address of a variable.
</p>

<p>Example:</p>

<pre><code>int a = 10;</code></pre>


