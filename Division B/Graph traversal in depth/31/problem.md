<div class="problem-statement">
   <div class="header">
      <h1 class="title">31. Поиск в глубину</h1>
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
         <p>Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности, содержащую
            первую вершину.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке записаны два целых числа <span class="tex-math-text">N</span> (<span class="tex-math-text">1 &le; N &le; 10<sup>3</sup></span>) и <span class="tex-math-text">M</span> (<span class="tex-math-text">0 &le; M &le; 5 * 10<sup>5</sup></span>)&nbsp;&mdash; количество вершин и ребер в графе. В последующих <span class="tex-math-text">M</span> строках перечислены ребра&nbsp;&mdash; пары чисел, определяющие номера вершин, которые соединяют ребра.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первую строку выходного файла выведите число <span class="tex-math-text">K</span>&nbsp;&mdash; количество вершин в компоненте связности. Во вторую строку выведите <span class="tex-math-text">K</span> целых чисел&nbsp;&mdash; вершины компоненты связности, перечисленные в порядке возрастания номеров.
         </p></span></div>
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
            <td><pre>4 5
2 2
3 4
2 3
1 3
2 4

</pre></td>
            <td><pre>4
1 2 3 4
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>