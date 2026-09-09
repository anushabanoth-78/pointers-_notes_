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
</section>
