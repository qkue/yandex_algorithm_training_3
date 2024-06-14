<div class="problem-statement">
   <div class="header">
      <h1 class="title">34. Топологическая сортировка</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Дан ориентированный граф. Необходимо построить топологическую сортировку.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла два натуральных числа <span class="tex-math-text">N</span> и <span class="tex-math-text">M</span> <span class="tex-math-text">(1 &le; N, M &le; 100&#8239;000)</span>&nbsp;&mdash; количество вершин и рёбер в графе соответственно. Далее в <span class="tex-math-text">M</span> строках перечислены рёбра графа. Каждое ребро задаётся парой чисел&nbsp;&mdash; номерами начальной и конечной вершин соответственно.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите любую топологическую сортировку графа в виде последовательности номеров вершин (перестановка чисел от 1 до N). Если
            топологическую сортировку графа построить невозможно, выведите -1. 
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
            <td><pre>6 6
1 2
3 2
4 2
2 5
6 5
4 6
</pre></td>
            <td><pre>4 6 3 1 2 5 
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
