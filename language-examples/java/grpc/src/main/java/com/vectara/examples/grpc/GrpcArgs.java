package com.vectara.examples.grpc;

import com.beust.jcommander.Parameter;
import javax.annotation.Nullable;

class GrpcArgs {
  @Parameter(
      names = {"--customer-id"},
      description = "Unique customer ID in Vectara platform.",
      required = true)
  Long customerId = null;

  @Parameter(
      names = {"--corpus-id"},
      description = "Corpus ID against which examples need to be run.",
      required = true)
  Long corpusId = 1L;

  @Parameter(
      names = {"--admin-endpoint"},
      description = "Admin endpoint such as admin.vectara.io")
  String adminEndpoint = "admin.vectara.io";

  @Parameter(
      names = {"--serving-endpoint"},
      description = "Serving endpoint such as serving.vectara.io")
  String servingEndpoint = "serving.vectara.io";

  @Parameter(
      names = {"--indexing-endpoint"},
      description = "Indexing endpoint such as indexing.vectara.io")
  String indexingEndpoint = "indexing.vectara.io";

  // Following args are required to obtain JWT Token.
  @Parameter(
      names = {"--auth-url"},
      description = "Authentication URL such as https://vectara-prod-{_CUSTOMER_ID}.auth.us-west-2.amazoncognito.com")
  String authUrl = "";

  @Parameter(
      names = {"--app-client-id"},
      description = "App Client ID retrieved from Vectara console.",
      required = true)
  @Nullable String appClientId;

  @Parameter(
      names = {"--app-client-secret"},
      description = "App client secret retrieved from Vectara console.",
      required = true)
  @Nullable String appClientSecret;

  @Parameter(
      names= {"--api-key"},
      description = "API key retrieved from Vectara console")
  @Nullable String apiKey = null;
}
