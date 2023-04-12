from dotenv import load_dotenv
import os
import openai

load_dotenv('.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

# https://platform.openai.com/docs/api-reference/requesting-organization
# print(openai.Model.list())

"""
{
  "data": [
    {
      "created": 1649358449,
      "id": "babbage",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1669085501,
          "group": null,
          "id": "modelperm-49FUp5v084tBB49tC4z8LPH5",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage"
    },
    {
      "created": 1649359874,
      "id": "davinci",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1669066355,
          "group": null,
          "id": "modelperm-U6ZwlyAd0LyMk4rcMdz33Yc3",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci"
    },
    {
      "created": 1649809179,
      "id": "text-davinci-edit-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1679934178,
          "group": null,
          "id": "modelperm-otmQSS0hmabtVGHI9QB3bct3",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-davinci-edit-001"
    },
    {
      "created": 1651172509,
      "id": "babbage-code-search-code",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669085863,
          "group": null,
          "id": "modelperm-4qRnA3Hj8HIJbgo0cGbcmErn",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage-code-search-code"
    },
    {
      "created": 1651172505,
      "id": "text-similarity-babbage-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669081947,
          "group": null,
          "id": "modelperm-48kcCHhfzvnfY84OtJf5m8Cz",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-similarity-babbage-001"
    },
    {
      "created": 1677610602,
      "id": "gpt-3.5-turbo",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1681168143,
          "group": null,
          "id": "modelperm-bLTRGdHW2gpCOsvg9LiXq7tX",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "gpt-3.5-turbo"
    },
    {
      "created": 1649880484,
      "id": "code-davinci-edit-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1679934178,
          "group": null,
          "id": "modelperm-Foe5Y4TvaKveYxt74oKMw8IB",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "code-davinci-edit-001"
    },
    {
      "created": 1649364042,
      "id": "text-davinci-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1669066355,
          "group": null,
          "id": "modelperm-MVM5NfoRjXkDve3uQW3YZDDt",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-davinci-001"
    },
    {
      "created": 1649357491,
      "id": "ada",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1675997661,
          "group": null,
          "id": "modelperm-u0nKN4ub7EVQudgMuvCuvDjc",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada"
    },
    {
      "created": 1651172509,
      "id": "babbage-code-search-text",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669085863,
          "group": null,
          "id": "modelperm-Lftf8H4ZPDxNxVs0hHPJBUoe",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage-code-search-text"
    },
    {
      "created": 1651172505,
      "id": "babbage-similarity",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669081947,
          "group": null,
          "id": "modelperm-mS20lnPqhebTaFPrcCufyg7m",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage-similarity"
    },
    {
      "created": 1677649963,
      "id": "gpt-3.5-turbo-0301",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1681168143,
          "group": null,
          "id": "modelperm-ktA0Xuzvxbe26mhuWenoLxx4",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "gpt-3.5-turbo-0301"
    },
    {
      "created": 1651172507,
      "id": "code-search-babbage-text-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669085863,
          "group": null,
          "id": "modelperm-EC5ASz4NLChtEV1Cwkmrwm57",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "code-search-babbage-text-001"
    },
    {
      "created": 1649364043,
      "id": "text-curie-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1679310997,
          "group": null,
          "id": "modelperm-8InhPV3CZfN3F5QHKoJd4zRD",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-curie-001"
    },
    {
      "created": 1677532384,
      "id": "whisper-1",
      "object": "model",
      "owned_by": "openai-internal",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1680896832,
          "group": null,
          "id": "modelperm-JdDYm8KjLd5xnGMGVlwX1UAp",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "whisper-1"
    },
    {
      "created": 1651172507,
      "id": "code-search-babbage-code-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669085864,
          "group": null,
          "id": "modelperm-64LWHdlANgak2rHzc3K5Stt0",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "code-search-babbage-code-001"
    },
    {
      "created": 1669599635,
      "id": "text-davinci-003",
      "object": "model",
      "owned_by": "openai-internal",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1680551675,
          "group": null,
          "id": "modelperm-eX6Zax2krvLf9WtfO3NN9YJh",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-davinci-003"
    },
    {
      "created": 1649364042,
      "id": "text-ada-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1669088497,
          "group": null,
          "id": "modelperm-KN5dRBCEW4az6gwcGXkRkMwK",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-ada-001"
    },
    {
      "created": 1671217299,
      "id": "text-embedding-ada-002",
      "object": "model",
      "owned_by": "openai-internal",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1678892857,
          "group": null,
          "id": "modelperm-Dbv2FOgMdlDjO8py8vEjD5Mi",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-embedding-ada-002"
    },
    {
      "created": 1651172505,
      "id": "text-similarity-ada-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092759,
          "group": null,
          "id": "modelperm-DdCqkqmORpqxqdg4TkFRAgmw",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-similarity-ada-001"
    },
    {
      "created": 1649364042,
      "id": "curie-instruct-beta",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1680267269,
          "group": null,
          "id": "modelperm-bsg59MlOi88CMf1MjnIKrT5a",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie-instruct-beta"
    },
    {
      "created": 1651172505,
      "id": "ada-code-search-code",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669087421,
          "group": null,
          "id": "modelperm-wa8tg4Pi9QQNaWdjMTM8dkkx",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada-code-search-code"
    },
    {
      "created": 1651172507,
      "id": "ada-similarity",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092759,
          "group": null,
          "id": "modelperm-LtSIwCEReeDcvGTmM13gv6Fg",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada-similarity"
    },
    {
      "created": 1651172507,
      "id": "code-search-ada-text-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669087421,
          "group": null,
          "id": "modelperm-JBssaJSmbgvJfTkX71y71k2J",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "code-search-ada-text-001"
    },
    {
      "created": 1651172505,
      "id": "text-search-ada-query-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092640,
          "group": null,
          "id": "modelperm-1YiiBMYC8it0mpQCBK7t8uSP",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-ada-query-001"
    },
    {
      "created": 1651172509,
      "id": "davinci-search-document",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066355,
          "group": null,
          "id": "modelperm-M43LVJQRGxz6ode34ctLrCaG",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-search-document"
    },
    {
      "created": 1651172510,
      "id": "ada-code-search-text",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669087421,
          "group": null,
          "id": "modelperm-kFc17wOI4d1FjZEaCqnk4Frg",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada-code-search-text"
    },
    {
      "created": 1651172507,
      "id": "text-search-ada-doc-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092640,
          "group": null,
          "id": "modelperm-kbHvYouDlkD78ehcmMOGdKpK",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-ada-doc-001"
    },
    {
      "created": 1649364042,
      "id": "davinci-instruct-beta",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1669066356,
          "group": null,
          "id": "modelperm-k9kuMYlfd9nvFiJV2ug0NWws",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-instruct-beta"
    },
    {
      "created": 1651172507,
      "id": "text-similarity-curie-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669079883,
          "group": null,
          "id": "modelperm-6dgTTyXrZE7d53Licw4hYkvd",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-similarity-curie-001"
    },
    {
      "created": 1651172507,
      "id": "code-search-ada-code-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669087421,
          "group": null,
          "id": "modelperm-8soch45iiGvux5Fg1ORjdC4s",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "code-search-ada-code-001"
    },
    {
      "created": 1651172505,
      "id": "ada-search-query",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092640,
          "group": null,
          "id": "modelperm-b753xmIzAUkluQ1L20eDZLtQ",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada-search-query"
    },
    {
      "created": 1651172505,
      "id": "text-search-davinci-query-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066353,
          "group": null,
          "id": "modelperm-9McKbsEYSaDshU9M3bp6ejUb",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-davinci-query-001"
    },
    {
      "created": 1651172509,
      "id": "curie-search-query",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1677273417,
          "group": null,
          "id": "modelperm-sIbfSwzVpVBtymQgOQSLBpxe",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie-search-query"
    },
    {
      "created": 1651172505,
      "id": "davinci-search-query",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066353,
          "group": null,
          "id": "modelperm-lYkiTZMmJMWm8jvkPx2duyHE",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-search-query"
    },
    {
      "created": 1651172510,
      "id": "babbage-search-document",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669084981,
          "group": null,
          "id": "modelperm-5qFV9kxCRGKIXpBEP75chmp7",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage-search-document"
    },
    {
      "created": 1651172507,
      "id": "ada-search-document",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669092640,
          "group": null,
          "id": "modelperm-8qUMuMAbo4EwedbGamV7e9hq",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada-search-document"
    },
    {
      "created": 1651172509,
      "id": "text-search-curie-query-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1677273417,
          "group": null,
          "id": "modelperm-Iion0NCpsXPNtIkQ0owQLi7V",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-curie-query-001"
    },
    {
      "created": 1651172509,
      "id": "text-search-babbage-doc-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669084981,
          "group": null,
          "id": "modelperm-ao2r26P2Th7nhRFleHwy2gn5",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-babbage-doc-001"
    },
    {
      "created": 1651172508,
      "id": "curie-search-document",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1677273417,
          "group": null,
          "id": "modelperm-LDsN5wW8eKVuh1OsyciHntE9",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie-search-document"
    },
    {
      "created": 1651172509,
      "id": "text-search-curie-doc-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1677273417,
          "group": null,
          "id": "modelperm-taUGRSku7bQLa24SNIwYPEsi",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-curie-doc-001"
    },
    {
      "created": 1651172509,
      "id": "babbage-search-query",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669084981,
          "group": null,
          "id": "modelperm-wSs1hMXDKsrcErlbN8HmzlLE",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage-search-query"
    },
    {
      "created": 1649364043,
      "id": "text-babbage-001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1675105935,
          "group": null,
          "id": "modelperm-a3Ph5FIBbJxsoA4wvx7VYC7R",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-babbage-001"
    },
    {
      "created": 1651172505,
      "id": "text-search-davinci-doc-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066353,
          "group": null,
          "id": "modelperm-qhSf1j2MJMujcu3t7cHnF1DN",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-davinci-doc-001"
    },
    {
      "created": 1651172509,
      "id": "text-search-babbage-query-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669084981,
          "group": null,
          "id": "modelperm-Kg70kkFxD93QQqsVe4Zw8vjc",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-search-babbage-query-001"
    },
    {
      "created": 1651172510,
      "id": "curie-similarity",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1675106290,
          "group": null,
          "id": "modelperm-zhWKExSloaQiJgzjVHFmh2wR",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie-similarity"
    },
    {
      "created": 1649359874,
      "id": "curie",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1675106503,
          "group": null,
          "id": "modelperm-oPaljeveTjEIDbhDjzFiyf4V",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie"
    },
    {
      "created": 1651172505,
      "id": "text-similarity-davinci-001",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066356,
          "group": null,
          "id": "modelperm-OvmcfYoq5V9SF9xTYw1Oz6Ue",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-similarity-davinci-001"
    },
    {
      "created": 1649880484,
      "id": "text-davinci-002",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1679355287,
          "group": null,
          "id": "modelperm-l4EU6QlN1HcS0so0jU16kyg8",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-davinci-002"
    },
    {
      "created": 1651172509,
      "id": "davinci-similarity",
      "object": "model",
      "owned_by": "openai-dev",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": true,
          "allow_view": true,
          "created": 1669066353,
          "group": null,
          "id": "modelperm-lYYgng3LM0Y97HvB5CDc8no2",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-similarity"
    },
    {
      "created": 1590625110,
      "id": "cushman:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": true,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1590625111,
          "group": null,
          "id": "snapperm-FAup8P1KqclNlTsunLDRiesT",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "cushman:2020-05-03"
    },
    {
      "created": 1607631625,
      "id": "ada:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1607631626,
          "group": null,
          "id": "snapperm-9TYofAqUs54vytKYL0IX91rX",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "ada:2020-05-03"
    },
    {
      "created": 1607632611,
      "id": "babbage:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1607632613,
          "group": null,
          "id": "snapperm-jaLAcmyyNuaVmalCE1BGTGwf",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "babbage:2020-05-03"
    },
    {
      "created": 1607632725,
      "id": "curie:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1607632727,
          "group": null,
          "id": "snapperm-bt6R8PWbB2SwK5evFo0ZxSs4",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie:2020-05-03"
    },
    {
      "created": 1607640163,
      "id": "davinci:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1607640164,
          "group": null,
          "id": "snapperm-99cbfQTYDVeLkTYndX3UMpSr",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci:2020-05-03"
    },
    {
      "created": 1610745990,
      "id": "if-davinci-v2",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1610746036,
          "group": null,
          "id": "snapperm-58q0TdK2K4kMgL3MoHvGWMlH",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "if-davinci-v2"
    },
    {
      "created": 1610745968,
      "id": "if-curie-v2",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1610746043,
          "group": null,
          "id": "snapperm-fwAseHVq6NGe6Ple6tKfzRSK",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "if-curie-v2"
    },
    {
      "created": 1629420755,
      "id": "if-davinci:3.0.0",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": true,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1629421809,
          "group": null,
          "id": "snapperm-T53lssiyMWwiuJwhyO9ic53z",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "if-davinci:3.0.0"
    },
    {
      "created": 1629498070,
      "id": "davinci-if:3.0.0",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": true,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1629498084,
          "group": null,
          "id": "snapperm-s6ZIAVMwlZwrLGGClTXqSK3Q",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-if:3.0.0"
    },
    {
      "created": 1629501914,
      "id": "davinci-instruct-beta:2.0.0",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": true,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1629501939,
          "group": null,
          "id": "snapperm-c70U4TBfiOD839xptP5pJzyc",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "davinci-instruct-beta:2.0.0"
    },
    {
      "created": 1641949608,
      "id": "text-ada:001",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1641949610,
          "group": null,
          "id": "snapperm-d2PSnwFG1Yn9of6PvrrhkBcU",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-ada:001"
    },
    {
      "created": 1641943966,
      "id": "text-davinci:001",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1641944340,
          "group": null,
          "id": "snapperm-Fj1O3zkKXOQy6AkcfQXRKcWA",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-davinci:001"
    },
    {
      "created": 1641955047,
      "id": "text-curie:001",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1641955123,
          "group": null,
          "id": "snapperm-BI9TAT6SCj43JRsUb9CYadsz",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-curie:001"
    },
    {
      "created": 1642018370,
      "id": "text-babbage:001",
      "object": "model",
      "owned_by": "openai",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1642018480,
          "group": null,
          "id": "snapperm-7oP3WFr9x7qf5xb3eZrVABAH",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "text-babbage:001"
    }
  ],
  "object": "list"
}
"""

# https://platform.openai.com/docs/libraries/python-library
response = openai.Completion.create(
    model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
print(response)
print(response['choices'][0].text)
import ipdb
ipdb.set_trace()
