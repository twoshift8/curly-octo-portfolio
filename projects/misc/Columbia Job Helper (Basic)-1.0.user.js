// ==UserScript==
// @name         Columbia Job Helper (Basic)
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Tick “Research” and open the top N Columbia listings on demand.
// @match        https://opportunities.columbia.edu/jobs/search*
// @grant        GM_openInTab
// @grant        GM_registerMenuCommand
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    function runHelper() {
        // 1) Tick the “Research” filter
        const resXPath = '/html/body/div[3]//fieldset/ul/li[18]/label/span[1]';
        const resSpan = document.evaluate(
            resXPath, document, null,
            XPathResult.FIRST_ORDERED_NODE_TYPE, null
        ).singleNodeValue;
        if (!resSpan) {
            alert("❌ Couldn’t find the Research checkbox!");
            return;
        }
        const chk = resSpan.previousElementSibling || resSpan;
        if (!chk.checked) chk.click();

        // 2) Ask how many to open
        let N = parseInt(prompt("How many top listings to open?", "5"), 10);
        if (isNaN(N) || N < 1) N = 5;

        // 3) Grab all job links
        const anchors = Array.from(document.querySelectorAll("a[id^='link_job_title']"));
        if (!anchors.length) {
            alert("⚠️ No job links found on this page.");
            return;
        }

        // 4) Slice out the top N and open each in a new tab
        anchors.slice(0, N).forEach(a => GM_openInTab(a.href, { active: true }));
        alert(`✅ Opened ${Math.min(N, anchors.length)} tab(s).`);
    }

    GM_registerMenuCommand("▶ Open Top N Columbia Listings", runHelper);
})();
