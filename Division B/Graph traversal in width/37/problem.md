<div class="problem-statement">
   <div class="header">
      <h1 class="title">37. Путь в графе</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Python 3.6</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
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
         <p>В неориентированном графе требуется найти минимальный путь между двумя вершинами.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности (0 обозначает
            отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной. 
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам путь. Если путь имеет длину
            0, то его выводить не нужно, достаточно вывести длину. 
         </p></span><p>Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.</p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>10
0 1 0 0 0 0 0 0 0 0
1 0 0 1 1 0 1 0 0 0
0 0 0 0 1 0 0 0 1 0
0 1 0 0 0 0 1 0 0 0
0 1 1 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 1 0 0 0 0 1 0 0
0 0 0 0 1 1 0 0 0 0
5 4
</pre></td>
            <td><pre>2
5 2 4</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>