class AIModel {
  String message;
  Map<String, dynamic> params;
  String nodeName;
  String nodeType;
  String task;
  int nodeId;

  AIModel({
    required this.message,
    required this.params,
    required this.nodeName,
    required this.nodeType,
    required this.task,
    required this.nodeId,
  });

  factory AIModel.fromJson(Map<String, dynamic> json) {
    return AIModel(
      message: json['message'],
      params: json['params'],
      nodeName: json['node_name'],
      nodeType: json['node_type'],
      task: json['task'],
      nodeId: json['node_id'],
    );
  }

  Map<String, dynamic> toJson() => {
        'message': message,
        'params': params,
        'node_name': nodeName,
        'node_type': nodeType,
        'task': task,
        'node_id': nodeId,
      };

  @override
  String toString() {
    // TODO: implement toString
    return 'AIModel: $nodeId';
  }
}
