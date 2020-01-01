/**
 * Adds cookie opt in banner to website.
 *
 * @uses cookieconsent - see https://cookieconsent.insites.com/documentation/disabling-cookies/
 */
( function () {
	window.addEventListener( "load", function () {
		window.cookieconsent.initialise( {
			"palette": {
				"popup": {
					"background": cdv8Gdpr.popupBackgroundColor,
					"text": cdv8Gdpr.popupTextColor
				},
				"button": {
					"background": cdv8Gdpr.btnBackgroundColor,
				}
			},
			"content": {
				"dismiss": cdv8Gdpr.dismissBtnText,
				"link": cdv8Gdpr.policyLinkText,
				"href": cdv8Gdpr.policyLinkTextURL,
				"message": cdv8Gdpr.bannerMessage
			}
		} );
	} );
} )();