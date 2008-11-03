<map version="0.8.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node COLOR="#000000" CREATED="1222267718506" ID="Freemind_Link_1303975272" MODIFIED="1223738067115" TEXT="ioflow&#xa;classes">
<font NAME="SansSerif" SIZE="20"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties"/>
<node COLOR="#0033ff" CREATED="1223737965706" ID="_" MODIFIED="1223749612475" POSITION="right" TEXT="TPad">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223748926685" ID="Freemind_Link_1448445587" MODIFIED="1223748984509" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223748988649" ID="Freemind_Link_126394850" MODIFIED="1223749472969" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947145" ID="Freemind_Link_442999715" MODIFIED="1223749483554" TEXT="name">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>name handle for pad</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947145" ID="Freemind_Link_1862342444" MODIFIED="1223749483559" TEXT="label">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>human readable name of pad (useful for labeling &quot;pins&quot;)</text>
</hook>
</node>
</node>
<node COLOR="#990000" CREATED="1223748992960" ID="Freemind_Link_972147859" MODIFIED="1223749491149" TEXT="variant">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947145" ID="Freemind_Link_1187669853" MODIFIED="1223749496649" TEXT="value">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>current value of data in pad</text>
</hook>
</node>
</node>
<node COLOR="#990000" CREATED="1223748995391" ID="Freemind_Link_518604989" MODIFIED="1223749499791" TEXT="numeric">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947145" ID="Freemind_Link_411619938" MODIFIED="1223749508969" TEXT="offset">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>+/- offset to add to the value before sending</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947147" ID="Freemind_Link_1966091437" MODIFIED="1223749508977" TEXT="keep alive">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>interval between re-sending of value (in msec)</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947147" ID="Freemind_Link_521013810" MODIFIED="1223749508984" TEXT="ramping">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>time delay between 2 values (in msec)</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947148" ID="Freemind_Link_1796369840" MODIFIED="1223749508990" TEXT="min">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>lower range limit</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947149" ID="Freemind_Link_1095815582" MODIFIED="1223749509000" TEXT="max">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>upper range limit</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947149" ID="Freemind_Link_275969843" MODIFIED="1223749509007" TEXT="precision">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>number of digits after the comma. &#xa;For floats.</text>
</hook>
</node>
</node>
<node COLOR="#990000" CREATED="1223748997237" ID="Freemind_Link_628376859" MODIFIED="1223749779231" TEXT="array of TPad">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947146" ID="Freemind_Link_317195503" MODIFIED="1223749524248" TEXT="pads">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>existing connections</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947146" ID="Freemind_Link_516991929" MODIFIED="1223749524253" TEXT="inputs">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>connections to listen to (filled once at runtime from &quot;self.pads&quot;)</text>
</hook>
</node>
<node COLOR="#111111" CREATED="1223748947146" ID="Freemind_Link_1240362137" MODIFIED="1223749524260" TEXT="outputs">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>connections to send to (filled once at runtime from &quot;self.pads&quot;)</text>
</hook>
</node>
</node>
<node COLOR="#990000" CREATED="1223749550749" ID="Freemind_Link_1463027899" MODIFIED="1223749563341" TEXT="option">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947147" ID="Freemind_Link_341130861" MODIFIED="1223749567923" TEXT="flow">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>data flow of pad: &quot;sink|source|both&quot;</text>
</hook>
<node COLOR="#111111" CREATED="1223749006213" ID="Freemind_Link_1973056562" MODIFIED="1223749727824" TEXT="[in|out|duplex]">
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node COLOR="#111111" CREATED="1223748947147" ID="Freemind_Link_1545721584" MODIFIED="1223749570830" TEXT="type">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>type </text>
</hook>
<node COLOR="#111111" CREATED="1223749016909" ID="Freemind_Link_482615575" MODIFIED="1223749027064" TEXT="[numeric|string|xxx]"/>
</node>
</node>
<node COLOR="#990000" CREATED="1223749036542" ID="Freemind_Link_1053614648" MODIFIED="1223749576084" TEXT="array of TPadFilter">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947148" ID="Freemind_Link_103494488" MODIFIED="1223749578903" TEXT="filter">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>filter &amp; manipulate data values&#xa;(array, because it&apos;s like an effect rack)</text>
</hook>
</node>
</node>
<node COLOR="#990000" CREATED="1223749034728" ID="Freemind_Link_1107039842" MODIFIED="1223749581817" TEXT="bool">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223748947148" ID="Freemind_Link_590031610" MODIFIED="1223749584051" TEXT="calibration">
<font NAME="SansSerif" SIZE="12"/>
<hook NAME="accessories/plugins/NodeNote.properties">
<text>auto calibration on/off</text>
</hook>
</node>
</node>
</node>
<node COLOR="#00b439" CREATED="1223749402621" HGAP="45" ID="Freemind_Link_1013928224" MODIFIED="1223749593399" TEXT="methods" VSHIFT="32">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749405044" ID="Freemind_Link_424715423" MODIFIED="1223749407567" TEXT="send()">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1223749408578" ID="Freemind_Link_1622695816" MODIFIED="1223749410678" TEXT="recv()">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1223749411341" ID="Freemind_Link_100698603" MODIFIED="1223749413139" TEXT="bang()">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223737976166" ID="Freemind_Link_574195745" MODIFIED="1223749632193" POSITION="left" TEXT="TElement">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223738033599" ID="Freemind_Link_464398727" MODIFIED="1223750193880" TEXT="children" VSHIFT="-122">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223738017675" ID="Freemind_Link_1913743654" MODIFIED="1223749756006" TEXT="TButton">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1223738020521" HGAP="29" ID="Freemind_Link_1710485399" MODIFIED="1223749758637" TEXT="TPixel" VSHIFT="-1">
<font NAME="SansSerif" SIZE="14"/>
</node>
<node COLOR="#990000" CREATED="1223738022760" ID="Freemind_Link_351435539" MODIFIED="1223749760899" TEXT="TFader">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1223738074068" ID="Freemind_Link_1140334825" MODIFIED="1223738078239" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749762822" ID="Freemind_Link_976401567" MODIFIED="1223749763923" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223738090740" ID="Freemind_Link_1315562802" MODIFIED="1223749792745" TEXT="label">
<font NAME="SansSerif" SIZE="12"/>
</node>
<node COLOR="#111111" CREATED="1223738085909" ID="Freemind_Link_1144469247" MODIFIED="1223749794415" TEXT="name">
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node COLOR="#990000" CREATED="1223749765362" ID="Freemind_Link_844101887" MODIFIED="1223749767359" TEXT="array of TPad">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223738093767" ID="Freemind_Link_79396464" MODIFIED="1223749790215" TEXT="pads">
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223737980057" ID="Freemind_Link_396544131" MODIFIED="1223749619284" POSITION="right" TEXT="THardware">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223749424539" ID="Freemind_Link_144703194" MODIFIED="1223749428872" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749598635" ID="Freemind_Link_672662814" MODIFIED="1223749601020" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223749866606" ID="Freemind_Link_708491285" MODIFIED="1223749868292" TEXT="name"/>
</node>
<node COLOR="#990000" CREATED="1223749601825" ID="Freemind_Link_222286806" MODIFIED="1223749606313" TEXT="array of TElement">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223749869012" ID="Freemind_Link_1597640612" MODIFIED="1223749870970" TEXT="elements"/>
</node>
</node>
<node COLOR="#00b439" CREATED="1223749885302" ID="Freemind_Link_1168289506" MODIFIED="1223749887441" TEXT="methods">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749888255" ID="Freemind_Link_560608710" MODIFIED="1223749893522" TEXT="getElementsByType()">
<font NAME="SansSerif" SIZE="14"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223737983798" ID="Freemind_Link_934261891" MODIFIED="1223750226932" POSITION="left" TEXT="TSoftware">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223749432763" ID="Freemind_Link_1482033349" MODIFIED="1223749434124" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223750173411" ID="Freemind_Link_1885727046" MODIFIED="1223750175055" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223750175725" ID="Freemind_Link_262203187" MODIFIED="1223750176546" TEXT="name"/>
<node COLOR="#111111" CREATED="1223750177406" ID="Freemind_Link_1943732955" MODIFIED="1223750178272" TEXT="label"/>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223738001821" ID="Freemind_Link_1581072630" MODIFIED="1223749622140" POSITION="right" TEXT="TWidget">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223738074068" ID="Freemind_Link_1693650947" MODIFIED="1223738078239" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749762822" ID="Freemind_Link_1145480362" MODIFIED="1223749763923" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223738090740" ID="Freemind_Link_1761564661" MODIFIED="1223749792745" TEXT="label">
<font NAME="SansSerif" SIZE="12"/>
</node>
<node COLOR="#111111" CREATED="1223738085909" ID="Freemind_Link_1919197727" MODIFIED="1223749794415" TEXT="name">
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node COLOR="#990000" CREATED="1223749765362" ID="Freemind_Link_307344222" MODIFIED="1223749767359" TEXT="array of TPad">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223738093767" ID="Freemind_Link_1448440668" MODIFIED="1223749790215" TEXT="pads">
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223738005786" HGAP="22" ID="Freemind_Link_1095479668" MODIFIED="1223750143128" POSITION="left" TEXT="TProtocol" VSHIFT="60">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223749435452" ID="Freemind_Link_113265111" MODIFIED="1223749436772" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
</node>
</node>
<node COLOR="#0033ff" CREATED="1223749652548" ID="Freemind_Link_84561633" MODIFIED="1223750087146" POSITION="right" TEXT="TPadFilter" VSHIFT="-17">
<font NAME="SansSerif" SIZE="18"/>
<node COLOR="#00b439" CREATED="1223749658609" ID="Freemind_Link_1329505976" MODIFIED="1223749660505" TEXT="properties">
<font NAME="SansSerif" SIZE="16"/>
<node COLOR="#990000" CREATED="1223749661890" ID="Freemind_Link_305648050" MODIFIED="1223749663576" TEXT="string">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223749672163" ID="Freemind_Link_857248601" MODIFIED="1223749673006" TEXT="name"/>
<node COLOR="#111111" CREATED="1223749678476" ID="Freemind_Link_748864176" MODIFIED="1223749679489" TEXT="label"/>
</node>
<node COLOR="#990000" CREATED="1223749664417" ID="Freemind_Link_1922456194" MODIFIED="1223749665547" TEXT="variant">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223749673889" ID="Freemind_Link_1912493012" MODIFIED="1223749685226" TEXT="in"/>
<node COLOR="#111111" CREATED="1223749686047" ID="Freemind_Link_1289769611" MODIFIED="1223749686763" TEXT="out"/>
</node>
<node COLOR="#990000" CREATED="1223749666346" ID="Freemind_Link_1537365889" MODIFIED="1223749670131" TEXT="array of variant">
<font NAME="SansSerif" SIZE="14"/>
<node COLOR="#111111" CREATED="1223749695690" ID="Freemind_Link_1000583856" MODIFIED="1223749696817" TEXT="old"/>
</node>
</node>
</node>
</node>
</map>
