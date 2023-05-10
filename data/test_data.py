test_data = [
    {
        "name": "test_cache_hit",
        "input": {
            "content_id": "abc123",
            "caches": [
                {"cache_type": "A", "ip": "10.0.0.1"},
                {"cache_type": "A", "ip": "10.0.0.2"},
                {"cache_type": "B", "ip": "192.168.0.1"}
            ],
            "client_ip": "192.168.1.1",
            "expected_cache_ip": "10.0.0.1"
        },
        "output": {
            "status_code": 200,
            "content": "test content",
            "cache_ip": "10.0.0.1",
            "hit": True
        }
    },
    {
        "name": "test_cache_miss",
        "input": {
            "content_id": "xyz789",
            "caches": [
                {"cache_type": "A", "ip": "10.0.0.3"},
                {"cache_type": "A", "ip": "10.0.0.4"},
                {"cache_type": "B", "ip": "192.168.0.2"}
            ],
            "client_ip": "192.168.1.2",
            "expected_cache_ip": "10.0.0.3"
        },
        "output": {
            "status_code": 200,
            "content": "test content",
            "cache_ip": "10.0.0.3",
            "hit": False
        }
    },
    {
        "name": "test_invalid_content_id",
        "input": {
            "content_id": "invalid123",
            "caches": [
                {"cache_type": "A", "ip": "10.0.0.5"},
                {"cache_type": "A", "ip": "10.0.0.6"},
                {"cache_type": "B", "ip": "192.168.0.3"}
            ],
            "client_ip": "192.168.1.3",
            "expected_cache_ip": None
        },
        "output": {
            "status_code": 404,
            "content": None,
            "cache_ip": None,
            "hit": None
        }
    }
]
