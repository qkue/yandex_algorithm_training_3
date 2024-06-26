<div class="problem-statement">
   <div class="header">
      <h1 class="title">3. Коллекционер Диего</h1>
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
         <p>Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер мечтает собрать наклейки
            со всеми встречающимися числами. 
         </p></span><p>Диего собрал <span class="tex-math-text">N</span> наклеек, некоторые из которых, возможно, совпадают. Как-то раз к нему пришли <span class="tex-math-text">K</span> коллекционеров. <span class="tex-math-text">i</span>-й из них собрал все наклейки с номерами не меньшими, чем <span class="tex-math-text">p<sub>i</sub></span>. Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего.
         Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке содержится единственное число <span class="tex-math-text">N</span> (<span class="tex-math-text">0 &le; N &le; 100&#8239;000</span>)&nbsp;&mdash; количество наклеек у Диего. 
         </p></span><p>В следующей строке содержатся <span class="tex-math-text">N</span> целых неотрицательных чисел (не обязательно различных)&nbsp;&mdash; номера наклеек Диего. Все номера наклеек не превосходят <span class="tex-math-text">10<sup>9</sup></span>. 
      </p>
      <p>В следующей строке содержится число <span class="tex-math-text">K</span> (<span class="tex-math-text">0 &le; K &le; 100&#8239;000</span>)&nbsp;&mdash; количество коллекционеров, пришедших к Диего. В следующей строке содержатся <span class="tex-math-text">K</span> целых чисел <span class="tex-math-text">p<sub>i</sub></span> (<span class="tex-math-text">0 &le; p<sub>i</sub> &le; 10<sup>9</sup></span>), где <span class="tex-math-text">p<sub>i</sub></span>&nbsp;&mdash; наименьший номер наклейки, не интересующий <span class="tex-math-text">i</span>-го коллекционера.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого коллекционера в отдельной строке выведите количество <span style="font-weight:bold;">различных</span> чисел на наклейках, которые есть у Диего, но нет у этого коллекционера.
         </p></span></div>
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
            <td><pre>1
5
2
4 6
</pre></td>
            <td><pre>0
1
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
            <td><pre>3
100 1 50
3
300 0 75
</pre></td>
            <td><pre>3
0
2
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
