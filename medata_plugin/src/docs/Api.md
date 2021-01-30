## Functions

<dl>
<dt><a href="#fetchMetadata">fetchMetadata(query)</a></dt>
<dd><p>Axios post request for sending current user URL to backend and recieves insight data for forwarded paper/ article URL.</p>
</dd>
<dt><a href="#fetchFurtherInformation">fetchFurtherInformation(query)</a></dt>
<dd><p>Axios post request for sending current user URL to backend and starting backend scraper to get further information.</p>
</dd>
<dt><a href="#postRateRelevanceInsight">postRateRelevanceInsight(inPaperId, inInsight, inUpvote)</a></dt>
<dd><p>Axios post request that sends an upvote (bolean) to highten relevance for certain insight selected by the user.</p>
</dd>
<dt><a href="#postAnswer">postAnswer(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Axios post request that sends new answer for an insight added by the user to the backend.</p>
</dd>
<dt><a href="#postRateAnswer">postRateAnswer(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Axios post request that sends the selected answer (rating for yellow-status inisghts) for an insight to the backend.</p>
</dd>
<dt><a href="#postInsight">postInsight(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Axios post request that sends new insight added by the user to the backend.</p>
</dd>
<dt><a href="#fetchDownload">fetchDownload(query)</a></dt>
<dd><p>Axios post request that sends current URL and recieves the .csv file with available insight data for direct-download.</p>
</dd>
<dt><a href="#postBinder">postBinder(binder)</a></dt>
<dd><p>Axios post request that sends <em>Binder</em> URL&#39;s to the backend for the multiple-paper direct-download.</p>
</dd>
<dt><a href="#postInsightNotRelevant">postInsightNotRelevant(inInsight, inCategories)</a></dt>
<dd><p>Axios post request that sends insight-not-relevant error to the backend so it can be handled.</p>
</dd>
<dt><a href="#postTypoError">postTypoError(inInsight)</a></dt>
<dd><p>Axios post request that sends typo-error to the backend so it can be handled by downvoting it double.</p>
</dd>
<dt><a href="#fetchAutocomplete">fetchAutocomplete(inCategories)</a></dt>
<dd><p>Axios post request that sends request for topic related keywoards for the autocompleate feature.</p>
</dd>
</dl>

<a name="fetchMetadata"></a>

## fetchMetadata(query)
Axios post request for sending current user URL to backend and recieves insight data for forwarded paper/ article URL.

**Kind**: global function  

| Param | Type |
| --- | --- |
| query | <code>String</code> | 

<a name="fetchFurtherInformation"></a>

## fetchFurtherInformation(query)
Axios post request for sending current user URL to backend and starting backend scraper to get further information.

**Kind**: global function  

| Param | Type |
| --- | --- |
| query | <code>String</code> | 

<a name="postRateRelevanceInsight"></a>

## postRateRelevanceInsight(inPaperId, inInsight, inUpvote)
Axios post request that sends an upvote (bolean) to highten relevance for certain insight selected by the user.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> | 
| inInsight | <code>String</code> | 
| inUpvote | <code>Boolean</code> | 

<a name="postAnswer"></a>

## postAnswer(inPaperId, inInsight, inAnswer)
Axios post request that sends new answer for an insight added by the user to the backend.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> | 
| inInsight | <code>String</code> | 
| inAnswer | <code>String</code> | 

<a name="postRateAnswer"></a>

## postRateAnswer(inPaperId, inInsight, inAnswer)
Axios post request that sends the selected answer (rating for yellow-status inisghts) for an insight to the backend.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> | 
| inInsight | <code>String</code> | 
| inAnswer | <code>String</code> | 

<a name="postInsight"></a>

## postInsight(inPaperId, inInsight, inAnswer)
Axios post request that sends new insight added by the user to the backend.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> | 
| inInsight | <code>String</code> | 
| inAnswer | <code>String</code> | 

<a name="fetchDownload"></a>

## fetchDownload(query)
Axios post request that sends current URL and recieves the .csv file with available insight data for direct-download.

**Kind**: global function  

| Param | Type |
| --- | --- |
| query | <code>String</code> | 

<a name="postBinder"></a>

## postBinder(binder)
Axios post request that sends _Binder_ URL's to the backend for the multiple-paper direct-download.

**Kind**: global function  

| Param | Type |
| --- | --- |
| binder | <code>Array</code> | 

<a name="postInsightNotRelevant"></a>

## postInsightNotRelevant(inInsight, inCategories)
Axios post request that sends insight-not-relevant error to the backend so it can be handled.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inInsight | <code>String</code> | 
| inCategories | <code>Array</code> | 

<a name="postTypoError"></a>

## postTypoError(inInsight)
Axios post request that sends typo-error to the backend so it can be handled by downvoting it double.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inInsight | <code>String</code> | 

<a name="fetchAutocomplete"></a>

## fetchAutocomplete(inCategories)
Axios post request that sends request for topic related keywoards for the autocompleate feature.

**Kind**: global function  

| Param | Type |
| --- | --- |
| inCategories | <code>Array</code> | 