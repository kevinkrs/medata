## Functions

<dl>
<dt><a href="#fetchMetadata">fetchMetadata(query)</a></dt>
<dd><p>axios post request for sending current user URL</p>
</dd>
<dt><a href="#fetchFurtherInformation">fetchFurtherInformation(query)</a></dt>
<dd><p>axios post request for sending current user URL and staring backend scraper to get further information</p>
</dd>
<dt><a href="#postRateRelevanceInsight">postRateRelevanceInsight(inPaperId, inInsight, inUpvote)</a></dt>
<dd><p>Sends an upvote to highten relevance for certain insight selected by the user</p>
</dd>
<dt><a href="#postAnswer">postAnswer(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Sends new answer for an insight added by the user to the backend</p>
</dd>
<dt><a href="#postRateAnswer">postRateAnswer(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Sends answer selection (rating) for an insight to the backend</p>
</dd>
<dt><a href="#postInsight">postInsight(inPaperId, inInsight, inAnswer)</a></dt>
<dd><p>Sends new insight added by the user to the backend</p>
</dd>
<dt><a href="#fetchDownload">fetchDownload(query)</a></dt>
<dd><p>Recieves the .csv file with available insight data for direct-download</p>
</dd>
<dt><a href="#postBinder">postBinder(binder)</a></dt>
<dd><p>Sends binder URL&#39;s to the backend for the multiple-paper direct-download</p>
</dd>
<dt><a href="#postInsightNotRelevant">postInsightNotRelevant(inInsight, inCategories)</a></dt>
<dd><p>Sends insight-not-relevant error to the backend so it can be handled by downvoting it double</p>
</dd>
<dt><a href="#postTypoError">postTypoError(inInsight)</a></dt>
<dd><p>Sends typo error to the backend so it can be handled by downvoting it double</p>
</dd>
<dt><a href="#fetchAutocomplete">fetchAutocomplete(inCategories)</a></dt>
<dd><p>Sends request for topic related keywoards for the autocompleate feature</p>
</dd>
</dl>

<a name="fetchMetadata"></a>

## fetchMetadata(query)
axios post request for sending current user URL

**Kind**: global function

| Param | Type |
| --- | --- |
| query | <code>String</code> |

<a name="fetchFurtherInformation"></a>

## fetchFurtherInformation(query)
axios post request for sending current user URL and staring backend scraper to get further information

**Kind**: global function

| Param | Type |
| --- | --- |
| query | <code>String</code> |

<a name="postRateRelevanceInsight"></a>

## postRateRelevanceInsight(inPaperId, inInsight, inUpvote)
Sends an upvote to highten relevance for certain insight selected by the user

**Kind**: global function

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> |
| inInsight | <code>String</code> |
| inUpvote | <code>Boolean</code> |

<a name="postAnswer"></a>

## postAnswer(inPaperId, inInsight, inAnswer)
Sends new answer for an insight added by the user to the backend

**Kind**: global function

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> |
| inInsight | <code>String</code> |
| inAnswer | <code>String</code> |

<a name="postRateAnswer"></a>

## postRateAnswer(inPaperId, inInsight, inAnswer)
Sends answer selection (rating) for an insight to the backend

**Kind**: global function

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> |
| inInsight | <code>String</code> |
| inAnswer | <code>String</code> |

<a name="postInsight"></a>

## postInsight(inPaperId, inInsight, inAnswer)
Sends new insight added by the user to the backend

**Kind**: global function

| Param | Type |
| --- | --- |
| inPaperId | <code>String</code> |
| inInsight | <code>String</code> |
| inAnswer | <code>String</code> |

<a name="fetchDownload"></a>

## fetchDownload(query)
Recieves the .csv file with available insight data for direct-download

**Kind**: global function

| Param | Type |
| --- | --- |
| query | <code>String</code> |

<a name="postBinder"></a>

## postBinder(binder)
Sends binder URL's to the backend for the multiple-paper direct-download

**Kind**: global function

| Param | Type |
| --- | --- |
| binder | <code>Array</code> |

<a name="postInsightNotRelevant"></a>

## postInsightNotRelevant(inInsight, inCategories)
Sends insight-not-relevant error to the backend so it can be handled by downvoting it double

**Kind**: global function

| Param | Type |
| --- | --- |
| inInsight | <code>String</code> |
| inCategories | <code>Array</code> |

<a name="postTypoError"></a>

## postTypoError(inInsight)
Sends typo error to the backend so it can be handled by downvoting it double

**Kind**: global function

| Param | Type |
| --- | --- |
| inInsight | <code>String</code> |

<a name="fetchAutocomplete"></a>

## fetchAutocomplete(inCategories)
Sends request for topic related keywoards for the autocompleate feature

**Kind**: global function

| Param | Type |
| --- | --- |
| inCategories | <code>Array</code> |
