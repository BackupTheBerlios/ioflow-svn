<map version="0.8.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node COLOR="#000000" CREATED="1222158434379" ID="Freemind_Link_1527470437" MODIFIED="1225717153222" TEXT="PyIO Flow &#xa;29.Sep.08">
<font NAME="SansSerif" SIZE="20"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties"/>
<node COLOR="#0033ff" CREATED="1222161152661" FOLDED="true" HGAP="184" ID="Freemind_Link_1684794993" MODIFIED="1222253063916" POSITION="left" TEXT="Data values" VSHIFT="2">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222161180630" ID="Freemind_Link_1018877894" MODIFIED="1222252683080" TEXT="types">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222161196867" ID="Freemind_Link_862680383" MODIFIED="1222252683085" TEXT="integer">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222161200410" ID="Freemind_Link_1483768422" MODIFIED="1222252683091" TEXT="float">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222161203261" ID="Freemind_Link_1329925166" MODIFIED="1222252683095" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222161209637" ID="Freemind_Link_175992259" MODIFIED="1222252683103" TEXT="array ?">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222162359789" ID="Freemind_Link_87074994" MODIFIED="1222252683110" TEXT="automatic conversion">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162303348" ID="Freemind_Link_515012710" MODIFIED="1222252683114" TEXT="pool mapping" VSHIFT="-34">
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Example:&#xa;&#xa;- Button:&#xa;each press transmits next value in the list: &#xa;[hihat, snare, bassdrum, ...]&#xa;&#xa;Options: &#xa;a) cycle (0,1,2,0,1,2,...)&#xa;b) mirror (0,1,2,1,0,1,2...)&#xa;</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1222165435122" ID="Freemind_Link_811533029" MODIFIED="1222252683116" TEXT="discrete &lt;=&gt; continous">
<node COLOR="#111111" CREATED="1222165500697" ID="Freemind_Link_1075716422" MODIFIED="1222252683118" TEXT="Fader &gt; x LEDs"/>
<node COLOR="#111111" CREATED="1222165516893" ID="Freemind_Link_227446723" MODIFIED="1222252683120" TEXT="x Buttons &gt; Fader value"/>
</node>
</node>
</node>
<node COLOR="#00b439" CREATED="1222162173175" ID="Freemind_Link_417065887" MODIFIED="1222252683124" TEXT="preprocessing">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222162183336" ID="Freemind_Link_315465251" MODIFIED="1222252683130" TEXT="ramping">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162282269" ID="Freemind_Link_413176324" MODIFIED="1222252683133" TEXT="output interval" VSHIFT="-20"/>
<node COLOR="#111111" CREATED="1222162822543" ID="Freemind_Link_786746738" MODIFIED="1222252683135" TEXT="duration"/>
</node>
<node COLOR="#990000" CREATED="1222162187393" ID="Freemind_Link_1747080340" MODIFIED="1222252683141" TEXT="filter">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162197683" ID="Freemind_Link_1882247504" MODIFIED="1222252683143" TEXT="threshold">
<node COLOR="#111111" CREATED="1222165642642" ID="Freemind_Link_241539997" MODIFIED="1222252683145" TEXT="absolute"/>
<node COLOR="#111111" CREATED="1222165647487" ID="Freemind_Link_83548314" MODIFIED="1222252683147" TEXT="differential"/>
</node>
<node COLOR="#111111" CREATED="1222165660256" ID="Freemind_Link_867470829" MODIFIED="1222252683149" TEXT="gateway"/>
</node>
<node COLOR="#990000" CREATED="1222162203890" ID="Freemind_Link_1319320965" MODIFIED="1222252683155" TEXT="jitter/noise reduction">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222165673339" ID="Freemind_Link_1175744748" MODIFIED="1222252683160" TEXT="joysticks"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222162431537" ID="Freemind_Link_731954981" MODIFIED="1222252683164" TEXT="transmission" VSHIFT="41">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222162445529" ID="Freemind_Link_964447488" MODIFIED="1222252683168" TEXT="when to send value?">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162462396" ID="Freemind_Link_520272611" MODIFIED="1222252683173" TEXT="triggered (bang!)">
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Send (transmit, output) a value if a certain pad is triggered.&#xa;Can be compared with PD&apos;s &quot;bang&quot; functionality.</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1222162473242" ID="Freemind_Link_979158546" MODIFIED="1222252683175" TEXT="autofire">
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Although the &quot;real&quot; autofire of a joystick actually toggles the button&apos;s value (0/1), &#xa;I think in our application it&apos;s better to just re-send the value as long as the input is in &quot;pressed&quot; state.&#xa;&#xa;So this would only apply to a button as far as I can see, because e.g. a fader doesn&apos;t have clearly defined &quot;on&quot; state. </text>
</hook>
</node>
<node COLOR="#111111" CREATED="1222162480014" ID="Freemind_Link_1254649196" MODIFIED="1222252683183" TEXT="keep-alive">
<hook NAME="accessories/plugins/NodeNote.properties">
<text>There might probably be some cases where a value should be sent although no user input has taken place. &#xa;This applies to *any* element, and is regardless of it&apos;s current &quot;state&quot; (e.g. pressed or released).&#xa;The sending interval should be configurable. &#xa;&#xa;This mechanism can also be used when ramping a value to configure how &apos;smooth&apos; the value update on the output will be.</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1222162694750" ID="Freemind_Link_1946979420" MODIFIED="1222252683185" TEXT="on change"/>
</node>
<node COLOR="#990000" CREATED="1222165409251" ID="Freemind_Link_1284245636" MODIFIED="1222252683189" TEXT="protocol">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222165680137" ID="Freemind_Link_29679100" MODIFIED="1222252683194" TEXT="auto calibration">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222165689885" ID="Freemind_Link_599005665" MODIFIED="1222252683199" TEXT="update min/max automatically">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222161354920" FOLDED="true" HGAP="72" ID="Freemind_Link_979209515" MODIFIED="1222262344723" POSITION="right" TEXT="Web ressources">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222161360297" HGAP="23" ID="Freemind_Link_310682686" MODIFIED="1222252683221" TEXT="brainstorming" VSHIFT="32">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222161366284" ID="Freemind_Link_1568262215" LINK="http://www.das-werkstatt.com/forum/werkstatt/viewtopic.php?t=495" MODIFIED="1222252683221" TEXT="das-werkstatt.com">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162954290" ID="Freemind_Link_60486715" MODIFIED="1222252683221" TEXT="^Rooker"/>
</node>
<node COLOR="#990000" CREATED="1222161556075" ID="Freemind_Link_595294227" LINK="http://post.monome.org/comments.php?DiscussionID=2297" MODIFIED="1222252683222" TEXT="monome.org">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222162930366" ID="Freemind_Link_1925664545" LINK="http://mediati.org/temp/router.html" MODIFIED="1222252683222" TEXT="mediati.org">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222162963401" ID="Freemind_Link_1171855619" MODIFIED="1222252683222" TEXT="Halex"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222163023938" ID="Freemind_Link_276719790" LINK="http://docs.monome.org/doku.php?id=frameworks:oscrouter" MODIFIED="1222252683222" TEXT="wiki">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222163529949" ID="Freemind_Link_1043397129" MODIFIED="1222252683223" TEXT="related">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222163537029" ID="Freemind_Link_685634832" LINK="http://www.steim.org/steim/junxion_v3.html" MODIFIED="1222252683223" TEXT="junXion">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163592095" ID="Freemind_Link_175168508" MODIFIED="1222252683223" TEXT="data routing app for OSX"/>
</node>
<node COLOR="#990000" CREATED="1222163547124" ID="Freemind_Link_1198116040" LINK="http://docs.monome.org/doku.php?id=app:serial-pyio" MODIFIED="1222252683224" TEXT="serial-pyio">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163606068" ID="Freemind_Link_1305014755" MODIFIED="1222252683224" TEXT="monomeserial clone with &quot;proxies&quot;"/>
</node>
<node COLOR="#990000" CREATED="1222163553359" ID="Freemind_Link_1022928748" LINK="http://post.monome.org/comments.php?DiscussionID=1153" MODIFIED="1222252683224" TEXT="OSC monitor &amp; utils">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163565529" ID="Freemind_Link_1794907213" LINK="http://carl.kenner.googlepages.com/glovepie" MODIFIED="1222252683224" TEXT="GlovePie">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163639573" ID="Freemind_Link_1569254579" MODIFIED="1222252683225" TEXT="programmable input emulator"/>
</node>
<node COLOR="#990000" CREATED="1222163570559" ID="Freemind_Link_232625301" LINK="http://hci.stanford.edu/research/istuff/ballagas2003a.pdf" MODIFIED="1222252683225" TEXT="iStuff">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163649223" ID="Freemind_Link_118214207" MODIFIED="1222252683225" TEXT="A Physical User Interface Toolkit for Ubiquitous Computing"/>
</node>
<node COLOR="#990000" CREATED="1222163574161" ID="Freemind_Link_1648208772" LINK="http://www.arduino.cc/playground/Interfacing/Firmata" MODIFIED="1222252683225" TEXT="Firmata">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163659174" ID="Freemind_Link_1869721944" MODIFIED="1222252683226" TEXT="Generic protocol for communicating with microcontrollers from software on a host computer"/>
</node>
<node COLOR="#990000" CREATED="1222163580583" ID="Freemind_Link_825629129" LINK="http://docs.monome.org/doku.php?id=app:mapd" MODIFIED="1222252683226" TEXT="mapd">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163667386" ID="Freemind_Link_331131509" MODIFIED="1222252683226" TEXT="long sleeping graphical widget interface"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222158434380" FOLDED="true" HGAP="204" ID="Freemind_Link_635282470" MODIFIED="1222253051739" POSITION="left" TEXT="Elements" VSHIFT="-4">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222160864538" ID="Freemind_Link_978762304" MODIFIED="1222252683243" TEXT="= basic archetypes of IO">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222161093647" ID="Freemind_Link_611344273" MODIFIED="1222252683250" TEXT="Pads">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222161099565" ID="Freemind_Link_1418943278" MODIFIED="1222252683257" TEXT="= Input/Output pins">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222165339932" ID="Freemind_Link_1308882622" MODIFIED="1222252683263" TEXT="self containing">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222165355102" ID="Freemind_Link_1590746801" MODIFIED="1222252683265" TEXT="knows about value types"/>
<node COLOR="#111111" CREATED="1222165041596" ID="Freemind_Link_228451817" MODIFIED="1222252683267" TEXT="automagic conversion">
<arrowlink DESTINATION="Freemind_Link_87074994" ENDARROW="Default" ENDINCLINATION="-185;0;" ID="Freemind_Arrow_Link_869958152" STARTARROW="None" STARTINCLINATION="65;-195;"/>
</node>
<node COLOR="#111111" CREATED="1222165561934" ID="Freemind_Link_1080328864" MODIFIED="1222252683269" TEXT="avoid invalid connections"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222160968596" HGAP="37" ID="Freemind_Link_1931644729" MODIFIED="1222252683274" TEXT="Types" VSHIFT="14">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222160943856" ID="Freemind_Link_121462549" MODIFIED="1222252683284" TEXT="Button">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222165887478" FOLDED="true" ID="Freemind_Link_475725564" MODIFIED="1222252683288" TEXT="state">
<node COLOR="#111111" CREATED="1222165891256" ID="Freemind_Link_190845501" MODIFIED="1222252683290" TEXT="on"/>
<node COLOR="#111111" CREATED="1222165893291" ID="Freemind_Link_1045282306" MODIFIED="1222252683292" TEXT="off"/>
</node>
</node>
<node COLOR="#990000" CREATED="1222160952795" ID="Freemind_Link_1205363327" MODIFIED="1222252683296" TEXT="LED (Pixel)">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222165802318" ID="Freemind_Link_1885239478" MODIFIED="1222252683308" TEXT="color (#RRGGBB)"/>
<node COLOR="#111111" CREATED="1222165812571" FOLDED="true" ID="Freemind_Link_1647182000" MODIFIED="1222252683309" TEXT="brightness ?">
<node COLOR="#111111" CREATED="1222165818625" ID="Freemind_Link_1498479592" MODIFIED="1222252683312" TEXT="could be handled with color"/>
</node>
<node COLOR="#111111" CREATED="1222165824707" FOLDED="true" ID="Freemind_Link_1953098442" MODIFIED="1222252683313" TEXT="on / off">
<node COLOR="#111111" CREATED="1222165828598" ID="Freemind_Link_1557871476" MODIFIED="1222252683315" TEXT="normal LED"/>
<node COLOR="#111111" CREATED="1222165859320" ID="Freemind_Link_1879602135" MODIFIED="1222252683317" TEXT="trigger previous color"/>
</node>
</node>
<node COLOR="#990000" CREATED="1222160958591" ID="Freemind_Link_1409383802" MODIFIED="1222252683324" TEXT="Fader">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222165731719" FOLDED="true" ID="Freemind_Link_1431676277" MODIFIED="1222252683327" TEXT="range">
<node COLOR="#111111" CREATED="1222165750451" ID="Freemind_Link_153671907" MODIFIED="1222252683329" TEXT="min"/>
<node COLOR="#111111" CREATED="1222165754606" ID="Freemind_Link_1383148033" MODIFIED="1222252683331" TEXT="max"/>
</node>
<node COLOR="#111111" CREATED="1222165766810" FOLDED="true" ID="Freemind_Link_1999914281" MODIFIED="1222252683333" TEXT="precision">
<node COLOR="#111111" CREATED="1222165785470" ID="Freemind_Link_1877507006" MODIFIED="1222252683336" TEXT="digits after the comma"/>
</node>
</node>
<node COLOR="#990000" CREATED="1222166572290" ID="Freemind_Link_470806777" MODIFIED="1222252683341" TEXT="Future ones">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222166582696" FOLDED="true" ID="Freemind_Link_132149746" MODIFIED="1222252683343" TEXT="character">
<node COLOR="#111111" CREATED="1222166624062" ID="Freemind_Link_1801504490" MODIFIED="1222252683345" TEXT="7 segment display"/>
<node COLOR="#111111" CREATED="1222166642962" ID="Freemind_Link_203399901" MODIFIED="1222252683346" TEXT="char on LCD display"/>
</node>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222253439308" FOLDED="true" HGAP="84" ID="Freemind_Link_1962355056" MODIFIED="1222254485768" POSITION="right" TEXT="Implementation" VSHIFT="-11">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222254560318" ID="Freemind_Link_460975933" MODIFIED="1222254563375" TEXT="Language">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222254566045" ID="Freemind_Link_126279627" MODIFIED="1222260844112" TEXT="Python">
<font NAME="SansSerif" SIZE="14"/>
<icon BUILTIN="button_ok"/>
<node COLOR="#111111" CREATED="1222255269857" ID="Freemind_Link_1336356442" MODIFIED="1222260824283" TEXT="+">
<node COLOR="#111111" CREATED="1222255276364" ID="Freemind_Link_543497172" MODIFIED="1222261047975" TEXT="platform independent"/>
<node COLOR="#111111" CREATED="1222255276365" ID="Freemind_Link_127210428" MODIFIED="1222261232605" TEXT="very easy to learn">
<node COLOR="#111111" CREATED="1222261225256" ID="Freemind_Link_1264046648" MODIFIED="1222261229200" TEXT="thus, easy to contribute"/>
<node COLOR="#111111" CREATED="1222261233303" ID="Freemind_Link_207564310" MODIFIED="1222261250980" TEXT="hop on/hop off development"/>
</node>
<node COLOR="#111111" CREATED="1222255276365" ID="Freemind_Link_316792266" MODIFIED="1222261045095" TEXT="great to maintain"/>
<node COLOR="#111111" CREATED="1222255276365" ID="Freemind_Link_1370057429" MODIFIED="1222261043324" TEXT="highly flexible"/>
<node COLOR="#111111" CREATED="1222255276366" ID="Freemind_Link_1427930076" MODIFIED="1222261053022" TEXT="popular (thus, well supported)"/>
<node COLOR="#111111" CREATED="1222255276366" ID="Freemind_Link_126673531" MODIFIED="1222261158620" TEXT="extensions in other languages possible">
<node COLOR="#111111" CREATED="1222261144742" ID="Freemind_Link_1369077086" MODIFIED="1222261154639" TEXT="speed critical parts in C++"/>
<node COLOR="#111111" CREATED="1222261164923" ID="Freemind_Link_1644937629" MODIFIED="1222261188647" TEXT="easy to wrap non-Python libs"/>
</node>
<node COLOR="#111111" CREATED="1222255276369" ID="Freemind_Link_1192804703" MODIFIED="1222261061556" TEXT="interactive reference docs can be in the code."/>
<node COLOR="#111111" CREATED="1222261258944" ID="Freemind_Link_1659014030" MODIFIED="1222261262296" TEXT="no compiling necessary"/>
</node>
<node COLOR="#111111" CREATED="1222254600825" ID="Freemind_Link_1651179022" MODIFIED="1222260821422" TEXT="-">
<node COLOR="#111111" CREATED="1222260619233" ID="Freemind_Link_1759612684" MODIFIED="1222260624697" TEXT="not automatically typesafe"/>
<node COLOR="#111111" CREATED="1222260626076" ID="Freemind_Link_758620264" MODIFIED="1222260655961" TEXT="packaging?"/>
<node COLOR="#111111" CREATED="1222260637705" ID="Freemind_Link_181992499" MODIFIED="1222260649632" TEXT="speed?"/>
<node COLOR="#111111" CREATED="1222260671978" ID="Freemind_Link_1224540403" MODIFIED="1222260695436" TEXT="requires Python installed">
<node COLOR="#111111" CREATED="1222261113630" ID="Freemind_Link_1971216872" MODIFIED="1222261116191" TEXT="right version!"/>
</node>
</node>
</node>
<node COLOR="#990000" CREATED="1222254570782" ID="Freemind_Link_1912565647" MODIFIED="1222254577670" TEXT="C / C++">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222254614322" ID="Freemind_Link_859585837" MODIFIED="1222254615964" TEXT="+"/>
<node COLOR="#111111" CREATED="1222254616702" ID="Freemind_Link_1038307096" MODIFIED="1222254618249" TEXT="-"/>
</node>
<node COLOR="#990000" CREATED="1222254584755" ID="Freemind_Link_1280352668" MODIFIED="1222254586973" TEXT="Java">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222254619431" ID="Freemind_Link_1899224953" MODIFIED="1222254620619" TEXT="+">
<node COLOR="#111111" CREATED="1222260956720" ID="Freemind_Link_470665003" MODIFIED="1222260959669" TEXT="typesafe"/>
<node COLOR="#111111" CREATED="1222260969811" ID="Freemind_Link_1358553827" MODIFIED="1222261071371" TEXT="platform independent"/>
<node COLOR="#111111" CREATED="1222261014623" ID="Freemind_Link_1263846862" MODIFIED="1222261040205" TEXT="popular"/>
</node>
<node COLOR="#111111" CREATED="1222254621521" ID="Freemind_Link_90522517" MODIFIED="1222254622470" TEXT="-">
<node COLOR="#111111" CREATED="1222261032152" ID="Freemind_Link_407129447" MODIFIED="1222261037955" TEXT="speed?"/>
<node COLOR="#111111" CREATED="1222261074986" ID="Freemind_Link_1487359012" MODIFIED="1222261079305" TEXT="packaging?"/>
<node COLOR="#111111" CREATED="1222261080052" ID="Freemind_Link_1135138170" MODIFIED="1222261082284" TEXT="requires JRE"/>
</node>
</node>
<node COLOR="#990000" CREATED="1222254587679" ID="Freemind_Link_1808712659" MODIFIED="1222254589613" TEXT="Processing">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222254623423" ID="Freemind_Link_494106916" MODIFIED="1222254624132" TEXT="+">
<node COLOR="#111111" CREATED="1222260911665" ID="Freemind_Link_888988227" MODIFIED="1222260915301" TEXT="Java-ish"/>
<node COLOR="#111111" CREATED="1222260916414" ID="Freemind_Link_1467360834" MODIFIED="1222260920693" TEXT="Easier than Java"/>
<node COLOR="#111111" CREATED="1222260969811" ID="Freemind_Link_1620080599" MODIFIED="1222260974124" TEXT="Platform independent"/>
</node>
<node COLOR="#111111" CREATED="1222254624912" ID="Freemind_Link_1946649642" MODIFIED="1222254625674" TEXT="-">
<node COLOR="#111111" CREATED="1222260864470" ID="Freemind_Link_63344595" MODIFIED="1222260885840" TEXT="not well known"/>
<node COLOR="#111111" CREATED="1222260931321" ID="Freemind_Link_1758256453" MODIFIED="1222260951163" TEXT="lacks functionality (libs)"/>
<node COLOR="#111111" CREATED="1222261129137" ID="Freemind_Link_1656597726" MODIFIED="1222261134271" TEXT="requires Processing installed"/>
</node>
</node>
</node>
<node COLOR="#00b439" CREATED="1222260733955" ID="Freemind_Link_283690918" MODIFIED="1222260754717" TEXT="platform independent">
<font NAME="SansSerif" SIZE="16"/>
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222158434379" FOLDED="true" HGAP="270" ID="Freemind_Link_1609192024" MODIFIED="1222261656256" POSITION="left" TEXT="Widgets" VSHIFT="2">
<font NAME="SansSerif" SIZE="18"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Widgets combine several Elements to give them some sort of &quot;meaning&quot; and also add more complex functionality.</text>
</hook>
<node COLOR="#00b439" CREATED="1222166402907" ID="Freemind_Link_1413887963" MODIFIED="1222252683383" TEXT="Button">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222168001304" ID="Freemind_Link_508082811" MODIFIED="1222252683389" TEXT="press &amp; release">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222168010941" ID="Freemind_Link_841386674" MODIFIED="1222252683393" TEXT="keep state">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222166407533" ID="Freemind_Link_598550021" MODIFIED="1222252683397" TEXT="Fader">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222166411196" ID="Freemind_Link_407989801" MODIFIED="1222252683410" TEXT="LED (Pixel)">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222167996612" ID="Freemind_Link_1394174887" MODIFIED="1222252683418" TEXT="blinking">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222166418277" ID="Freemind_Link_667461869" MODIFIED="1222252683424" TEXT="Radiogroup">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222168030001" ID="Freemind_Link_1225857420" MODIFIED="1222252683433" TEXT="LED meter">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222168035813" ID="Freemind_Link_476806605" MODIFIED="1222252683437" TEXT="button slider">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222167987302" ID="Freemind_Link_1059497773" MODIFIED="1222252683441" TEXT="Counter">
<font NAME="SansSerif" SIZE="16"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222160650511" FOLDED="true" HGAP="175" ID="_" MODIFIED="1222261659009" POSITION="left" TEXT="Devices&#xa;(aka Hardware)" VSHIFT="-5">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222160790190" ID="Freemind_Link_1203400330" MODIFIED="1222252682860" TEXT="Device driver">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222163749772" ID="Freemind_Link_1619449999" MODIFIED="1222252682871" TEXT="OS specific">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163775672" ID="Freemind_Link_298293384" MODIFIED="1222252682882" TEXT="protocol?">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222160994332" ID="Freemind_Link_521172710" LINK="#Freemind_Link_635282470" MODIFIED="1222252682910" TEXT="break into Elements">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222163065538" FOLDED="true" ID="Freemind_Link_1721356874" MODIFIED="1222252682926" TEXT="examples">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222163081922" ID="Freemind_Link_18146924" MODIFIED="1222252682933" TEXT="wii-mote">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163090288" ID="Freemind_Link_486270778" MODIFIED="1222252682933" TEXT="joystick">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163146079" ID="Freemind_Link_1316677157" MODIFIED="1222252682934" TEXT="2 faders"/>
<node COLOR="#111111" CREATED="1222163151578" ID="Freemind_Link_809606244" MODIFIED="1222252682934" TEXT="4 buttons"/>
</node>
<node COLOR="#990000" CREATED="1222163096785" ID="Freemind_Link_1752883152" MODIFIED="1222252682934" TEXT="mouse">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163157253" ID="Freemind_Link_1202620841" MODIFIED="1222252682935" TEXT="2 faders"/>
<node COLOR="#111111" CREATED="1222163160109" ID="Freemind_Link_1322613244" MODIFIED="1222252682935" TEXT="3 buttons"/>
</node>
<node COLOR="#990000" CREATED="1222163098929" ID="Freemind_Link_1280867686" MODIFIED="1222252682936" TEXT="monome">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222163178149" ID="Freemind_Link_1865518942" MODIFIED="1222252682936" TEXT="40h">
<node COLOR="#111111" CREATED="1222163180374" ID="Freemind_Link_1503185502" MODIFIED="1222252682936" TEXT="64 buttons"/>
<node COLOR="#111111" CREATED="1222163193735" ID="Freemind_Link_486791508" MODIFIED="1222252682936" TEXT="64 LEDs"/>
</node>
</node>
<node COLOR="#990000" CREATED="1222163107685" ID="Freemind_Link_655372570" MODIFIED="1222252682937" TEXT="arduino-based">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222158434380" FOLDED="true" HGAP="207" ID="Freemind_Link_121921690" MODIFIED="1222261654121" POSITION="left" TEXT="Protocols" VSHIFT="-4">
<font NAME="SansSerif" SIZE="18"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Protocols shall be used to communicate with:&#xa;- devices&#xa;- applications&#xa;&#xa;Keep that in mind when creating protocol classes.</text>
</hook>
<node COLOR="#00b439" CREATED="1222160674647" ID="Freemind_Link_37930844" MODIFIED="1222252682730" TEXT="OSC">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222167101477" ID="Freemind_Link_1136020140" MODIFIED="1222252682738" TEXT="parameters">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222167106692" ID="Freemind_Link_704746533" MODIFIED="1222252682748" TEXT="send">
<node COLOR="#111111" CREATED="1222167115885" ID="Freemind_Link_700205993" MODIFIED="1222252682750" TEXT="host"/>
<node COLOR="#111111" CREATED="1222167142332" ID="Freemind_Link_1217221899" MODIFIED="1222252682752" TEXT="port"/>
</node>
<node COLOR="#111111" CREATED="1222167113789" ID="Freemind_Link_913662393" MODIFIED="1222252682756" TEXT="receive">
<node COLOR="#111111" CREATED="1222167144645" ID="Freemind_Link_1861648727" MODIFIED="1222252682758" TEXT="host"/>
<node COLOR="#111111" CREATED="1222167148860" ID="Freemind_Link_1368301738" MODIFIED="1222252682760" TEXT="port"/>
</node>
<node COLOR="#111111" CREATED="1222167166502" ID="Freemind_Link_1100851881" MODIFIED="1222252682762" TEXT="prefix"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222160678173" ID="Freemind_Link_37996184" MODIFIED="1222252682766" TEXT="MIDI">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222254654446" ID="Freemind_Link_941253236" MODIFIED="1222254662388" TEXT="parameters">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222254663244" ID="Freemind_Link_1039683321" MODIFIED="1222254664707" TEXT="channel"/>
<node COLOR="#111111" CREATED="1222254665503" ID="Freemind_Link_1328293401" MODIFIED="1222254671085" TEXT="note"/>
<node COLOR="#111111" CREATED="1222254671815" ID="Freemind_Link_1719379637" MODIFIED="1222254673575" TEXT="velocity"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222160682995" ID="Freemind_Link_933681791" MODIFIED="1222252682782" TEXT="xyz">
<font NAME="SansSerif" SIZE="16"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222162976170" FOLDED="true" HGAP="205" ID="Freemind_Link_845600312" MODIFIED="1222261663644" POSITION="right" TEXT="Contributors" VSHIFT="-12">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222260246800" ID="Freemind_Link_1998730418" MODIFIED="1222260377175" TEXT="^rooker">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260250528" ID="Freemind_Link_1855709116" MODIFIED="1222260363785" TEXT="halex">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260278872" ID="Freemind_Link_354687010" MODIFIED="1222260379501" TEXT="xndr">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260300403" ID="Freemind_Link_1741438740" MODIFIED="1222260385369" TEXT="jul">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260340744" ID="Freemind_Link_1706693192" MODIFIED="1222260350343" TEXT="ucacjbs">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260352807" ID="Freemind_Link_1842163239" MODIFIED="1222260355726" TEXT="stigi">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260357073" ID="Freemind_Link_1252293141" MODIFIED="1222260360461" TEXT="melka">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260390018" ID="Freemind_Link_528597071" MODIFIED="1222260391979" TEXT="tehn">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260393095" ID="Freemind_Link_557312042" MODIFIED="1222260401210" TEXT="crunchy_alligator">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260402374" ID="Freemind_Link_1384626760" MODIFIED="1222260405670" TEXT="julienb">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222260428199" ID="Freemind_Link_49274893" MODIFIED="1222260430235" TEXT="dseaver">
<font NAME="SansSerif" SIZE="16"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222158434380" FOLDED="true" HGAP="114" ID="Freemind_Link_168972063" MODIFIED="1222261650881" POSITION="left" TEXT="Applications" VSHIFT="-10">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222160932641" ID="Freemind_Link_1342972818" MODIFIED="1222252683454" TEXT="Name">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222162137503" ID="Freemind_Link_66161038" MODIFIED="1222252683459" TEXT="Define controls">
<font NAME="SansSerif" SIZE="16"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222162879415" FOLDED="true" HGAP="205" ID="Freemind_Link_101612864" MODIFIED="1222261667641" POSITION="right" TEXT="Name?" VSHIFT="-8">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222163935297" ID="Freemind_Link_882063611" MODIFIED="1222252683366" TEXT="Multifunctional Protocol Router">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222163994350" ID="Freemind_Link_647762087" LINK="http://digitalmedia.oreilly.com/2004/12/29/flow_1204.html" MODIFIED="1222252683366" TEXT="Something related with &#x201d;flow&#x201d;">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222164988348" ID="Freemind_Link_46756798" MODIFIED="1222252683367" TEXT="pyio-flow">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222165098029" FOLDED="true" ID="Freemind_Link_157308340" MODIFIED="1222252683367" TEXT="ambiguous">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222162884635" ID="Freemind_Link_1380288716" MODIFIED="1222252683368" TEXT="octine">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163946459" ID="Freemind_Link_1415096797" MODIFIED="1222252683370" TEXT="Protocol Mapper">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222164022023" ID="Freemind_Link_1734444406" MODIFIED="1222252683370" TEXT="transLator">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163977030" ID="Freemind_Link_1508666954" MODIFIED="1222252683370" TEXT="CrossTalk">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222165105007" FOLDED="true" ID="Freemind_Link_1475812247" MODIFIED="1222252683371" TEXT="taken">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222162895494" ID="Freemind_Link_976925203" MODIFIED="1222252683371" TEXT="prohto">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163930041" ID="Freemind_Link_24355393" MODIFIED="1222252683371" TEXT="ProtoCall">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222165150246" ID="Freemind_Link_520031275" MODIFIED="1222252683372" TEXT="MappR">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222163969922" ID="Freemind_Link_548317710" MODIFIED="1222252683372" TEXT="multiMapper">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222165120833" ID="Freemind_Link_980933927" MODIFIED="1222252683372" TEXT="protoMap">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1222165190712" FOLDED="true" ID="Freemind_Link_1708542194" MODIFIED="1222252683373" TEXT="outdated">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222163954032" ID="Freemind_Link_651036726" MODIFIED="1222252683373" TEXT="multifunctional bi-directional protocol translator">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1222246373070" FOLDED="true" HGAP="180" ID="Freemind_Link_1108619512" MODIFIED="1222261670037" POSITION="right" TEXT="Focus &amp; Goals" VSHIFT="8">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1222246387632" ID="Freemind_Link_1811118450" MODIFIED="1222252682949" TEXT="simplicity &gt; features">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222247067748" ID="Freemind_Link_592175009" MODIFIED="1222252682958" TEXT="rapid prototyping">
<font NAME="SansSerif" SIZE="16"/>
</node>
<node COLOR="#00b439" CREATED="1222247141615" ID="Freemind_Link_1526408191" MODIFIED="1222252682965" TEXT="separation">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1222247157769" ID="Freemind_Link_1586582558" MODIFIED="1222252682971" TEXT="GUI (patch editor)">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247164201" ID="Freemind_Link_292693377" MODIFIED="1222252682987" TEXT="headless engine">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247446822" ID="Freemind_Link_1798011080" MODIFIED="1222252682994" TEXT="technically skilled people">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247467097" ID="Freemind_Link_1666799095" MODIFIED="1222252683001" TEXT="artist">
<font NAME="SansSerif" SIZE="14"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>It shall be possible for a non-techie to use the framework!&#xa;Things like max/msp or pd require more technical skills than one might think.&#xa;&#xa;Connecting elements, widgets and applications must be made in a way accessible for everyone.</text>
</hook>
</node>
</node>
<node COLOR="#00b439" CREATED="1222247171605" ID="Freemind_Link_882900328" MODIFIED="1222252683008" TEXT="reusability">
<font NAME="SansSerif" SIZE="16"/>
<icon BUILTIN="messagebox_warning"/>
<node COLOR="#990000" CREATED="1222247204702" ID="Freemind_Link_370070568" MODIFIED="1222252683013" TEXT="coding only once!">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222247729020" ID="Freemind_Link_1448433641" MODIFIED="1222252683016" TEXT="devices"/>
<node COLOR="#111111" CREATED="1222247732076" ID="Freemind_Link_1744795990" MODIFIED="1222252683018" TEXT="elements"/>
<node COLOR="#111111" CREATED="1222247734546" ID="Freemind_Link_480183076" MODIFIED="1222252683020" TEXT="protocols"/>
<node COLOR="#111111" CREATED="1222247743079" ID="Freemind_Link_962505970" MODIFIED="1222252683024" TEXT="widgets"/>
</node>
<node COLOR="#990000" CREATED="1222247255025" ID="Freemind_Link_189737060" MODIFIED="1222252683030" TEXT="application mapping">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247766363" ID="Freemind_Link_423634444" MODIFIED="1222252683035" TEXT="share patches">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1222247831159" ID="Freemind_Link_1684340943" MODIFIED="1222252683037" TEXT="OS issues?"/>
<node COLOR="#111111" CREATED="1222247849762" ID="Freemind_Link_1443162867" MODIFIED="1222252683038" TEXT="plug &amp; play"/>
</node>
<node COLOR="#990000" CREATED="1222255324565" ID="Freemind_Link_1035186521" MODIFIED="1222255444238" TEXT="portable extensions">
<font NAME="SansSerif" SIZE="14"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>Improvements must be easy to share. &#xa;In case of new code (devices, elements, etc...) they should be plugin-in style.</text>
</hook>
</node>
</node>
<node COLOR="#00b439" CREATED="1222247274489" ID="Freemind_Link_436360690" MODIFIED="1222252683042" TEXT="quick start">
<font NAME="SansSerif" SIZE="16"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>A powerful application without presets is too overwhelming.&#xa;Think about a synthesizer:&#xa;Without presets, probably only tech freaks would be using them. :)</text>
</hook>
<node COLOR="#990000" CREATED="1222247282924" ID="Freemind_Link_1745108006" MODIFIED="1222252683049" TEXT="examples">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247292973" ID="Freemind_Link_421423761" MODIFIED="1222252683059" TEXT="presets">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1222247880395" ID="Freemind_Link_201316525" MODIFIED="1222252683065" TEXT="plug &amp; play">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
</node>
</map>
