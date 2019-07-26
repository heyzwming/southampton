from nose.tools import assert_equal
from sailing_robot.gps_utils import ubx_checksum

def test_ubx_checksum():
    assert_equal(ubx_checksum(b'\x06\x01\x08\x00\xF0\x02\x00\x00\x00\x00\x00\x01'),
                    b'\x02\x32')
    assert_equal(ubx_checksum(b'\x06\x01\x08\x00\xF0\x03\x00\x00\x00\x00\x00\x01'),
                    b'\x03\x39')
    assert_equal(ubx_checksum(b'\x06\x01\x08\x00\xF0\x04\x00\x00\x00\x00\x00\x01'),
                    b'\x04\x40')
    assert_equal(ubx_checksum(b'\x06\x01\x08\x00\xF0\x05\x00\x00\x00\x00\x00\x01'),
                    b'\x05\x47')
    assert_equal(ubx_checksum(b'\x06\x01\x08\x00\xF0\x01\x00\x00\x00\x00\x00\x01'),
                    b'\x01\x2B')
    assert_equal(ubx_checksum(b'\x06\x08\x06\x00\xC8\x00\x01\x00\x01\x00'),
                    b'\xDE\x6A')