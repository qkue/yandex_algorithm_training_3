<div class="problem-statement">
   <div class="header">
      <h1 class="title">32. Компоненты связности</h1>
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
         <p>Дан неориентированный невзвешенный граф, состоящий из <span class="tex-math-text">N</span> вершин и <span class="tex-math-text">M</span> ребер. Необходимо посчитать количество его компонент связности и вывести их.
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входном файле записано два числа N и M (0 &lt; N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два числа i
            и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром. 
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем
            формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке. 
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
            <td><pre>6 4
3 1
1 2
5 4
2 3
</pre></td>
            <td><pre>3
3
1 2 3 
2
4 5 
1
6 
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
            <td><pre>6 4
4 2
1 4
6 4
3 6
</pre></td>
            <td><pre>2
5
1 2 3 4 6 
1
5 
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
