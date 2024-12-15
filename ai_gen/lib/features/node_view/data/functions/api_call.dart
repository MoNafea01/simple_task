import 'package:ai_gen/core/classes/json_class.dart';
import 'package:ai_gen/core/classes/model_class.dart';
import 'package:dio/dio.dart';

class ApiCall {
  Future<Map<String, dynamic>> _makeAPICall(
    String endpoint, {
    required Map<String, dynamic> data,
    Map<String, dynamic> Function(Map<String, dynamic>)? processResponse,
  }) async {
    final dio = Dio();

    try {
      final response = await dio.post(
        "http://127.0.0.1:8000/$endpoint/",
        data: data,
        options: Options(contentType: Headers.jsonContentType),
      );

      if (response.statusCode == 200 || response.statusCode == 201) {
        final jsonResponse = Map<String, dynamic>.from(response.data);

        // Process response if a processor function is provided
        if (processResponse != null) {
          return processResponse(jsonResponse);
        }

        return jsonResponse;
      } else {
        throw Exception('Failed to perform the operation');
      }
    } on DioException catch (e) {
      if (e.response != null) {
        throw Exception(
            'Failed to perform the operation: ${e.response?.statusCode}');
      } else {
        throw Exception('Network error: ${e.message}');
      }
    }
  }

  Future<Map<String, dynamic>> trainTestSplit(
    List<dynamic> data, {
    double testSize = 0.2,
    int? randomState,
  }) async {
    return await _makeAPICall(
      'train_test_split',
      data: {
        'data': data,
        'test_size': testSize,
        'random_state': randomState,
      },
      processResponse: (response) => {
        'X_train': List<dynamic>.from(response['train_data']),
        'X_test': List<dynamic>.from(response['test_data']),
      },
    );
  }

  Future<Map<String, dynamic>> fitModel(
    AIModel model,
    Nafe3 x,
    Nafe3 y,
  ) async {
    return await _makeAPICall(
      'train_test_split',
      data: {
        'X': x,
        'y': y,
        'model': model.toJson(),
      },
      processResponse: (response) => {
        'X_train': List<dynamic>.from(response['train_data']),
        'X_test': List<dynamic>.from(response['test_data']),
      },
    );
  }
}
