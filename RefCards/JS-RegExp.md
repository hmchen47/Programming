# JavaSceipt - Regular Expression


## Reference: Methods for regular expressions in JavaScript

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y22np4b5">Methods using regular expressions</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Method</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
  </tr>
  </thead>
  <tbody>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec"><code>exec()</code></a></td><td>Executes a search for a match in a string. It returns an array of information or <code>null</code> on a mismatch.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test"><code>test()</code></a></td><td>Tests for a match in a string. It returns <code>true</code> or <code>false</code>.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match"><code>match()</code></a></td><td>Returns an array containing all of the matches, including capturing groups, or <code>null</code> if no match is found.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll"><code>matchAll()</code></a></td><td>Returns an iterator containing all of the matches, including capturing groups.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search"><code>search()</code></a></td><td>Tests for a match in a string. It returns the index of the match, or <code>-1</code> if the search fails.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace"><code>replace()</code></a></td><td>Executes a search for a match in a string, and replaces the matched substring with a replacement substring.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll"><code>replaceAll()</code></a></td><td>Executes a search for all matches in a string, and replaces the matched substrings with a replacement substring.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split"><code>split()</code></a></td><td>Uses a regular expression or a fixed string to break a string into an array of substrings.</td></tr>
  </tbody>
</table>





## Reference: Special characters in regular expressions

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y9jzpgll">Special characters in regular expressions</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Characters</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Meaning</th>
  </tr>
  </thead>
  <tbody>
    <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/yxtgs26n">Character Classes</a></th></tr>
		<tr>
			<td><code>.</code></td>
			<td>
			<p>Has one of the following meanings:</p>
			<ul>
				<li>Matches any single character <em>except</em> line terminators: <code>\n</code>, <code>\r</code>, <code>\u2028</code> or <code>\u2029</code>.&nbsp;For example, <code>/.y/</code> matches "my" and "ay", but not "yes", in "yes make my day".</li>
				<li>Inside a character set, the dot loses its special meaning and matches a literal dot.</li>
			</ul>
			<p>Note that the <code>m</code> multiline flag doesn't change the dot behavior. So to match a pattern across multiple lines, the character set <code>[^]</code> can be used — it will match any character including newlines.</p>
			<p>ES2018 added&nbsp;the <code>s</code> "dotAll" flag, which allows the dot to also match line terminators.</p>
			</td>
		</tr>
		<tr>
			<td><code>\d</code></td>
			<td>
			<p>Matches any digit (Arabic numeral). Equivalent to <code>[0-9]</code>. For example, <code>/\d/</code> or <code>/[0-9]/</code> matches "2" in "B2 is the suite number".</p>
			</td>
		</tr>
		<tr>
			<td><code>\D</code></td>
			<td>
			<p>Matches any character that is not a digit (Arabic numeral). Equivalent to <code>[^0-9]</code>. For example, <code>/\D/</code> or <code>/[^0-9]/</code> matches "B" in "B2 is the suite number".</p>
			</td>
		</tr>
		<tr>
			<td><code>\w</code></td>
			<td>
			<p>Matches any alphanumeric character from the basic Latin alphabet, including the underscore. Equivalent to <code>[A-Za-z0-9_]</code>. For example, <code>/\w/</code> matches "a" in "apple", "5" in "$5.28", "3" in "3D" and "m" in "Émanuel".</p>
			</td>
		</tr>
		<tr>
			<td><code>\W</code></td>
			<td>
			<p>Matches any character that is not a word character from the basic Latin alphabet. Equivalent to <code>[^A-Za-z0-9_]</code>. For example, <code>/\W/</code> or <code>/[^A-Za-z0-9_]/</code> matches "%" in "50%" and "É" in "Émanuel".</p>
			</td>
		</tr>
		<tr>
			<td><code>\s</code></td>
			<td>
			<p>Matches a single white space character, including space, tab, form feed, line feed, and other Unicode spaces. Equivalent to <code>[ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]</code>. For example, <code>/\s\w*/</code> matches " bar" in "foo bar".</p>
			</td>
		</tr>
		<tr>
			<td><code>\S</code></td>
			<td>
			<p>Matches a single character other than white space. Equivalent to <code>[^ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]</code>. For example, <code>/\S\w*/</code> matches "foo" in "foo bar".</p>
			</td>
		</tr>
		<tr><td><code>\t</code></td><td>Matches a horizontal tab.</td></tr>
		<tr><td><code>\r</code></td><td>Matches a carriage return.</td></tr>
		<tr><td><code>\n</code></td><td>Matches a linefeed.</td></tr>
		<tr><td><code>\v</code></td><td>Matches a vertical tab.</td></tr>
		<tr><td><code>\f</code></td><td>Matches a form-feed.</td></tr>
		<tr>
			<td><code>[\b]</code></td>
			<td>Matches a backspace. If you're looking for the word-boundary character (<code>\b</code>), see <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Boundaries">Boundaries</a>.</td>
		</tr>
		<tr><td><code>\0</code></td><td>Matches a NUL character. Do not follow this with another digit.</td></tr>
		<tr>
			<td><code>\c<em>X</em></code></td>
			<td>
			<p>Matches a control character using <a class="external" href="https://en.wikipedia.org/wiki/Caret_notation" rel="noopener">caret notation</a>, where "X" is a letter from A–Z (corresponding to codepoints <code>U+0001</code><em>–</em><code>U+001F</code>). For example, <code>/\cM/</code>&nbsp;matches "\r"&nbsp;in&nbsp;"\r\n".</p>
			</td>
		</tr>
		<tr><td><code>\x<em>hh</em></code></td><td>Matches the character with the code <code><em>hh</em></code> (two hexadecimal digits).</td></tr>
		<tr><td><code>\u<em>hhhh</em></code></td><td>Matches a UTF-16 code-unit with the value <code><em>hhhh</em></code> (four hexadecimal digits).</td>
		</tr>
		<tr><td><code>\u<em>{hhhh} </em>or <em>\u{hhhhh}</em></code></td><td>(Only when the <code>u</code> flag is set.) Matches the character with the Unicode value <code>U+<em>hhhh</em></code> or&nbsp;<code>U+<em>hhhhh</em></code> (hexadecimal digits).</td>
		</tr>
		<tr><td><code>\</code></td><td>
			<p>Indicates that the following character should be treated specially, or "escaped". It behaves one of two ways.</p>
			<ul>
				<li>For characters that are usually treated literally, indicates that the next character is special and not to be interpreted literally. For example, <code>/b/</code> matches the character "b". By placing a backslash in front of "b", that is by using <code>/\b/</code>, the character becomes special to mean match a word boundary.</li>
				<li>For characters that are usually treated specially, indicates that the next character is not special and should be interpreted literally. For example, "*" is a special character that means 0 or more occurrences of the preceding character should be matched; for example, <code>/a*/</code> means match 0 or more "a"s. To match <code>*</code> literally, precede it with a backslash; for example, <code>/a\*/</code> matches "a*".</li>
			</ul>
			<div class="blockIndicator note">
			<p>To match this character literally, escape it with itself. In other words to search for <code>\</code>&nbsp;use <code>/\\/</code>.</p>
			</div>
			</td>
		</tr>
    <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4lgft7c">Boundary-type Assertions</a></th></tr>
  <tr><td><code>^</code></td><td>
    <p>Matches the beginning of input. If the multiline flag is set to true, also matches immediately after a line break character. For example, <code>/^A/</code> does not match the "A" in "an A", but does match the first "A" in "An A".</p>
    <div class="blockIndicator note">
    <p>This character has a different meaning when it appears at the start of a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Groups_and_Ranges">group</a>.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>$</code></td><td>
    <p>Matches the end of input. If the multiline flag is set to true, also matches immediately before a line break character. For example, <code>/t$/</code> does not match the "t" in "eater", but does match it in "eat".</p>
   </td>
  </tr>
  <tr><td><code>\b</code></td><td>
    <p>Matches a word boundary. This is the position where a word character is not followed or preceded by another word-character, such as between a letter and a space. Note that a matched word boundary is not included in the match. In other words, the length of a matched word boundary is zero.</p>
    <p>Examples:</p>
    <ul>
     <li><code>/\bm/</code>&nbsp;matches the "m" in "moon".</li>
     <li><code>/oo\b/</code>&nbsp;does not match the "oo" in "moon", because "oo" is followed by "n" which is a word character.</li>
     <li><code>/oon\b/</code>&nbsp;matches the "oon" in "moon", because "oon" is the end of the string, thus not followed by a word character.</li>
     <li><code>/\w\b\w/</code>&nbsp;will never match anything, because a word character can never be followed by both a non-word and a word character.</li>
    </ul>
    <p>To match a backspace character (<code>[\b]</code>), see <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes">Character Classes</a>.</p>
   </td>
  </tr>
  <tr><td><code>\B</code></td><td>
    <p>Matches a non-word boundary. This is a position where the previous and next character are of the same type: Either both must be words, or both must be non-words, for example between two letters or between two spaces.&nbsp;The beginning and end of a string are considered non-words. Same as the matched word boundary, the matched non-word boundary is also not included in the match. For example, <code>/\Bon/</code> matches "on" in "at noon", and <code>/ye\B/</code> matches "ye" in "possibly yesterday".</p>
   </td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4lgft7c">Boundary-type Assertions</a></th></tr>
  <tr><td><code>x(?=y)</code></td><td>
    <p><strong>Lookahead assertion:&nbsp;</strong>Matches "x" only if "x" is followed by "y". For example, /<code>Jack(?=Sprat)/</code> matches "Jack" only if it is followed by "Sprat".<br>
     <code>/Jack(?=Sprat|Frost)/</code> matches "Jack" only if it is followed by "Sprat" or "Frost". However, neither "Sprat" nor "Frost" is part of the match results.</p>
   </td>
  </tr>
  <tr><td><code>x(?!y)</code></td><td>
    <p><strong>Negative lookahead assertion:&nbsp;</strong>Matches "x" only if "x"<span> is not followed by </span>"y"<span>.</span>&nbsp;For example, <code>/\d+(?!\.)/</code><span> matches a number only if it is not followed by a decimal point.&nbsp;</span><code>/\d+(?!\.)/.exec('3.141')</code> matches "141" but not "3.</p>
   </td>
  </tr>
  <tr><td><code>(?&lt;=y)x</code></td><td>
    <p><strong>Lookbehind assertion:&nbsp;</strong>Matches "x" only if "x" is preceded&nbsp;by "y".&nbsp;For example, <code>/(?&lt;=Jack)Sprat/</code><span> matches "Sprat" only if it is preceded by "Jack".&nbsp;</span><code>/(?&lt;=Jack|Tom)Sprat/</code> matches "Sprat" only if it is preceded by "Jack" or "Tom". However, neither "Jack" nor "Tom" is part of the match results.</p>
   </td>
  </tr>
  <tr>
   <td><code>(?&lt;!y)x</code></td>
   <td>
    <p><strong>Negative lookbehind assertion:&nbsp;</strong>Matches "x" only if "x" is not preceded&nbsp;by "y".&nbsp;For example, <code>/(?&lt;!-)\d+/</code><span> matches a number only if it is not preceded by a minus sign.&nbsp;</span><code>/(?&lt;!-)\d+/.exec('3')</code> matches "3".&nbsp;<code>/(?&lt;!-)\d+/.exec('-3')</code> &nbsp;match is not found because the&nbsp;number is preceded by the minus sign.</p>
   </td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4687y4a">Groups and Ranges</a></th></tr>
  <tr><td><code><em>x</em>|<em>y</em></code></td><td>
    <p>Matches either "x" or "y". For example, <code>/green|red/</code> matches "green" in "green apple" and "red" in "red apple".</p>
   </td>
  </tr>
  <tr>
   <td><code>[xyz]<br>
    [a-c]</code></td>
   <td>
    <p>A character set. Matches any one of the enclosed characters. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first or last character enclosed in the square brackets it is taken as a literal hyphen to be included in the character set as a normal character. It is also possible to include a character class in a character set.</p>
    <p>For example, <code>[abcd]</code> is the same as <code>[a-d]</code>. They match the "b" in "brisket", and the "c" in "chop".</p>
    <p>For example, <code>[abcd-]</code> and <code>[-abcd]</code> match the "b" in "brisket", the "c" in "chop", and the "-" (hyphen) in "non-profit".</p>
    <p>For example, <code>[\w-]</code> is the same as <code>[A-Za-z0-9_-]</code>. They both match the "b" in "brisket", the "c" in "chop", and the "n" in "non-profit".</p>
   </td>
  </tr>
  <tr>
   <td>
    <p><code>[^xyz]<br>
     [^a-c]</code></p>
   </td>
   <td>
    <p>A negated or complemented character set. That is, it matches anything that is not enclosed in the brackets. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first or last character enclosed in the square brackets it is taken as a literal hyphen to be included in the character set as a normal character. For example, <code>[^abc]</code> is the same as <code>[^a-c]</code>. They initially match "o" in "bacon" and "h" in "chop".</p>
    <div class="blockIndicator note">
    <p>The ^ character may also indicate the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Boundaries">beginning of input</a>.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>(<em>x</em>)</code></td><td>
    <p><strong>Capturing group:&nbsp;</strong>Matches <code><em>x</em></code> and remembers the match. For example, <code>/(foo)/</code> matches and remembers "foo" in "foo bar".&nbsp;</p>
    <p>A regular expression may have multiple capturing groups. In results, matches to capturing groups typically in an array whose members are in the same order as the left parentheses in the capturing group. This is usually just the order of the capturing groups themselves. This becomes important when capturing groups are nested. Matches are accessed using the index of the the result's elements (<code>[1], ..., [n]</code>) or from the predefined <code>RegExp</code> object's properties (<code>$1, ..., $9</code>).</p>
    <p>Capturing groups have a performance penalty. If you don't need the matched substring to be recalled, prefer non-capturing parentheses (see below).</p>
    <p><code><a href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match">String.match()</a></code> won't return groups if the <code>/.../g</code> flag is set. However, you can still use <code><a href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll">String.matchAll()</a></code> to get all matches.</p>
   </td>
  </tr>
  <tr><td><code>\<em>n</em></code></td><td>
    <p>Where "n" is a positive integer. A back reference to the last substring matching the n parenthetical in the regular expression (counting left parentheses). For example, <code>/apple(,)\sorange\1/</code> matches "apple, orange," in "apple, orange, cherry, peach".</p>
   </td>
  </tr>
  <tr><td><code>\k&lt;Name&gt;</code></td><td>
    <p>A back reference to the last substring matching the <strong>N</strong><strong>amed capture&nbsp;group </strong>specified by <code>&lt;Name&gt;</code>.</p>
    <p>For example, <code>/(?&lt;title&gt;\w+), yes \k&lt;title&gt;/</code>&nbsp;matches "Sir, yes Sir" in "Do you copy? Sir, yes Sir!".</p>
    <div class="blockIndicator note">
    <p><code>\k</code> is&nbsp;used literally here to indicate the beginning of a back reference to a Named capture group.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>(?&lt;Name&gt;x)</code></td><td>
    <p><strong>Named capturing group:&nbsp;</strong>Matches "x" and stores it on the groups property of the returned matches under the name specified by <code>&lt;Name&gt;</code>. The angle brackets (<code>&lt;</code> and <code>&gt;</code>) are required for group name.</p>
    <p>For example, to extract the United States area code from a phone number, we could use <code>/\((?&lt;area&gt;\d\d\d)\)/</code>. The resulting number would appear under <code>matches.groups.area</code>.</p>
   </td>
  </tr>
  <tr><td><code>(?:<em>x</em>)</code></td><td><strong>Non-capturing group:&nbsp;</strong>Matches "x" but does not remember the match. The matched substring cannot be recalled from the resulting array's elements (<code>[1], ..., [n]</code>) or from the predefined <code>RegExp</code> object's properties (<code>$1, ..., $9</code>).</td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y3k4gtxx">Quantifiers</a></th></tr>
  <tr><td><code><em>x</em>*</code></td><td>
    <p>Matches the preceding item "x" 0 or more times. For example, <code>/bo*/</code> matches "boooo" in "A ghost booooed" and "b" in "A bird warbled", but nothing in "A goat grunted".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>+</code></td><td>
    <p>Matches the preceding item "x" 1 or more times. Equivalent to <code>{1,}</code>. For example, <code>/a+/</code> matches the "a" in "candy" and all the "a"'s in "caaaaaaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>?</code></td><td>
    <p>Matches the preceding item "x" 0 or 1 times. For example, <code>/e?le?/</code> matches the "el" in "angel" and the "le" in "angle."</p>
    <p>If used immediately after any of the quantifiers <code>*</code>, <code>+</code>, <code>?</code>, or <code>{}</code>, makes the quantifier non-greedy (matching the minimum number of times), as opposed to the default, which is greedy (matching the maximum number of times).</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>}</code></td><td>
    <p>Where "n" is a positive integer, matches exactly "n" occurrences of the preceding item "x". For example, <code>/a{2}/</code> doesn't match the "a" in "candy", but it matches all of the "a"'s in "caandy", and the first two "a"'s in "caaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>,}</code></td><td>
    <p>Where "n" is a positive integer, matches at least "n" occurrences of the preceding item "x". For example, <code>/a{2,}/</code> doesn't match the "a" in "candy", but matches all of the a's in "caandy" and in "caaaaaaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>,<em>m</em>}</code></td><td>
    <p>Where "n" is 0 or a positive integer, "m" is a positive integer, and <code><em>m</em> &gt; <em>n</em></code>, matches at least "n" and at most "m" occurrences of the preceding item "x". For example, <code>/a{1,3}/</code> matches nothing in "cndy", the "a" in "candy", the two "a"'s in "caandy", and the first three "a"'s in "caaaaaaandy". Notice that when matching "caaaaaaandy", the match is "aaa", even though the original string had more "a"s in it.</p>
   </td>
  </tr>
  <tr>
   <td><p><code><em>x</em>*?</code><br><code><em>x</em>+?</code><br><code><em>x</em>??</code><br><code><em>x</em>{n}?</code><br><code><em>x</em>{n,}?</code><br><code><em>x</em>{n,m}?</code></p></td><td>
    <p>By default quantifiers like <code>*</code> and <code>+</code> are "greedy", meaning that they try to match as much of the string as possible. The <code>?</code> character after the quantifier makes the quantifier "non-greedy": meaning that it will stop as soon as it finds a match. For example, given a string like "some &lt;foo&gt; &lt;bar&gt; new &lt;/bar&gt; &lt;/foo&gt; thing":</p>
    <ul>
     <li><code>/&lt;.*&gt;/</code> will match "&lt;foo&gt; &lt;bar&gt; new &lt;/bar&gt; &lt;/foo&gt;"</li>
     <li><code>/&lt;.*?&gt;/</code> will match "&lt;foo&gt;"</li>
    </ul>
   </td>
  </tr>
  </tbody>
</table><br/>


