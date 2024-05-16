<div class="problem-statement">
   <div class="header">
      <h1 class="title">6. Операционные системы lite</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
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
         <p>Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные операционные системы следующим
            методом: он создавал новый раздел диска из последовательных секторов, начиная с сектора номер <span class="tex-math-text">a<sub>i</sub></span> и до сектора <span class="tex-math-text">b<sub>i</sub></span> включительно, и устанавливал на него очередную систему. При этом, если очередной раздел хотя бы по одному сектору пересекается
            с каким-то ранее созданным разделом, то ранее созданный раздел «затирается», и операционная система, которая на него была
            установлена, больше не может быть загружена.
         </p></span><p>Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит, сколько в итоге работоспособных
         операционных систем установлено и работает в настоящий момент на Васином компьютере. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся натуральное число M — количество секторов на жестком диске (1 ≤ M ≤ <span class="tex-math-text">10<sup>9</sup></span>) и целое число N — количество разделов, которое последовательно создавал Вася (0 ≤ N ≤ 1000).
         </p></span><p>Далее идут N пар чисел <span class="tex-math-text">a<sub>i</sub></span> и <span class="tex-math-text">b<sub>i</sub></span>, задающих номера начального и конечного секторов раздела (1 ≤ <span class="tex-math-text">a<sub>i</sub></span> ≤ <span class="tex-math-text">b<sub>i</sub></span> ≤ M). 
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число — количество работающих операционных систем на Васином компьютере.</p></span></div>
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
            <td><pre>10
3
1 3
4 7
3 4
</pre></td>
            <td><pre>1
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
            <td><pre>10
4
1 3
4 5
7 8
4 6
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
