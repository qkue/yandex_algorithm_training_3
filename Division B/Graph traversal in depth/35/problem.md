<div class="problem-statement">
   <div class="header">
      <h1 class="title">35. Поиск цикла</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Python 3.6</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его. </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке дано одно число n — количество вершин в графе ( 1 ≤ n ≤ 500 ). Далее в n строках задан сам граф матрицей смежности.           
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Если в иcходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй строке выведите число
            k — количество вершин в цикле, а в третьей строке выведите k различных чисел — номера вершин, которые принадлежат циклу в
            порядке обхода (обход можно начинать с любой вершины цикла). Если циклов несколько, то выведите любой. 
         </p></span><p></p>
   </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>3
0 1 1
1 0 1
1 1 0
</pre></td>
            <td><pre>YES
3
3 2 1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>4
0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0
</pre></td>
            <td><pre>NO
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5
0 1 0 0 0
1 0 0 0 0
0 0 0 1 1
0 0 1 0 1
0 0 1 1 0
</pre></td>
            <td><pre>YES
3
5 4 3
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
