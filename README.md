# Send Budget: remaining-send calculator widget

A hosted worksheet for newsletter authors, educators and bloggers who want readers to check whether a campaign fits the email sends left in their current cycle.

This repository provides embed instructions and an operator-owned demonstration. It is maintained with Send Budget; it is not an independent review or evidence that another publisher has adopted the widget.

[Try the embedded demonstration](https://kumiromiscythespec.github.io/send-budget-widget/).

[Use the full calculator](https://send-budget-1109.crisp-llama-2628.chatgpt.site/capacity.html?utm_source=github&utm_medium=referral#remaining-send-balance) · [Embed instructions on Send Budget](https://send-budget-1109.crisp-llama-2628.chatgpt.site/capacity.html#embed-calculator)

## Add it to a page

Copy the contents of [copied-snippet.txt](copied-snippet.txt) into an HTML/embed block on a page you control:

On the [demonstration page](https://kumiromiscythespec.github.io/send-budget-widget/), open **View the embed code** to select and copy the same snippet without downloading it.

```html
<iframe
  src="https://send-budget-1109.crisp-llama-2628.chatgpt.site/embed/remaining-sends.html"
  title="Remaining-send balance calculator by Send Budget"
  style="width:100%;height:1000px;border:0"
  loading="lazy"
  referrerpolicy="no-referrer"
  sandbox="allow-scripts"></iframe>
<p><a href="https://send-budget-1109.crisp-llama-2628.chatgpt.site/capacity.html?utm_source=github&amp;utm_medium=referral#remaining-send-balance" rel="noreferrer">Open the full remaining-send calculator on Send Budget</a></p>
```

Preview the published page on desktop and mobile. Adjust the height if needed and keep scrolling enabled. Some editors remove iframes or restrict external content; use the ordinary full-tool link when embedding is unavailable. The link stays outside the sandboxed iframe and needs no popup permission.

The live widget is hosted by Send Budget. This repository does not contain an offline calculator or a copy of its calculation JavaScript. The standalone widget requires JavaScript and initializes with example counts.

## On a site you already publish with Carrd

Carrd's [custom-code instructions](https://carrd.com/docs/building/embedding-custom-code) require **Pro Standard or higher** for an Embed element. If your current setup cannot embed the widget, publish an ordinary link to the full calculator instead.

1. In Carrd, choose **Add Element → Embed**, then set **Type: Code** and **Style: Inline**.
2. Paste the complete snippet above, including its fallback link. Keep the frame's scrolling available and adjust its height if your layout needs it.
3. Preview the **published page** on desktop and mobile. Carrd says custom code does not render inside its builder. Check that the four input labels, result and fallback link remain usable.

For an ordinary link, use `https://send-budget-1109.crisp-llama-2628.chatgpt.site/capacity.html#remaining-send-balance` as a link or button destination in your editor. Readers can use the hosted calculator without installing it. Keep your existing setup when a link is enough.

If you are already evaluating paid Carrd features, [Page Scope's feature and plan guide](https://page-scope-1109.crisp-llama-2628.chatgpt.site/pricing.html) can help distinguish Free, Lite, Standard and Plus requirements. Page Scope is maintained by the same operator and contains disclosed Carrd referral links. This guide is an ordinary link; the widget and snippet contain no affiliate links.

Carrd documentation checked 10 November 2026. These are documented setup steps; this repository's live demo remains the operator-owned GitHub Pages installation.

## What the worksheet checks

Enter four whole-number counts: the current remaining sends, the next campaign's sendable recipients, the total reserved for all planned resends, and other sends before the same reset. Enter an explicit `0` for none; a blank is unknown. Each input accepts 0–1,000,000,000.

- **Needed sends** = campaign + reserved resends + other sends.
- **Balance after the plan** = remaining sends − needed sends.
- **Shortfall** = the amount by which needed sends exceed the remaining balance, or zero.

For example, 10,000 remaining sends minus 5,000 campaign sends, 2,500 resend sends and 1,000 other sends leaves 1,500. The resend reserve may include multiple repeats; it is not limited to the size of the first campaign.

Check the live balance, reset and counting rules in your own provider's account. This arithmetic does not verify account approval, daily caps, sending speed or delivery, calculate fees, or recommend a paid plan.

## Privacy and hosting

The widget's four counts stay in its page memory. They are not saved, added to its URL or sent by the calculation code. The widget does not load Send Budget's aggregate page-use counting script or include affiliate links. Do not enter subscriber addresses or other private records.

Loading the iframe still requests public HTML, CSS and JavaScript from Send Budget's host. GitHub and hosting/security infrastructure can process normal request data under their own policies. The supplied iframe suppresses the referring-page URL; it does not pass a publisher identifier or calculation inputs.

The optional full-tool link has fixed `github` / `referral` source labels. Opening it loads a normal Send Budget page with the aggregate counts described in the [privacy notice](https://send-budget-1109.crisp-llama-2628.chatgpt.site/privacy.html). Those counts do not establish unique readers, sales or earnings.

## Local content check

Run `python check_distribution.py` with Python 3. It checks only this repository's HTML and snippet contracts. It makes no network request and does not verify browser rendering, third-party adoption, traffic or revenue.
