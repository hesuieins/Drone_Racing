# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from quadrotor_msgs/TRPYCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import quadrotor_msgs.msg
import std_msgs.msg

class TRPYCommand(genpy.Message):
  _md5sum = "6779ee8a86cc757aeea21725df32d00c"
  _type = "quadrotor_msgs/TRPYCommand"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float32 thrust
float32 roll
float32 pitch
float32 yaw
quadrotor_msgs/AuxCommand aux

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: quadrotor_msgs/AuxCommand
float64 current_yaw
float64 kf_correction
float64[2] angle_corrections# Trims for roll, pitch
bool enable_motors
bool use_external_yaw
"""
  __slots__ = ['header','thrust','roll','pitch','yaw','aux']
  _slot_types = ['std_msgs/Header','float32','float32','float32','float32','quadrotor_msgs/AuxCommand']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,thrust,roll,pitch,yaw,aux

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TRPYCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.thrust is None:
        self.thrust = 0.
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.aux is None:
        self.aux = quadrotor_msgs.msg.AuxCommand()
    else:
      self.header = std_msgs.msg.Header()
      self.thrust = 0.
      self.roll = 0.
      self.pitch = 0.
      self.yaw = 0.
      self.aux = quadrotor_msgs.msg.AuxCommand()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4f2d().pack(_x.thrust, _x.roll, _x.pitch, _x.yaw, _x.aux.current_yaw, _x.aux.kf_correction))
      buff.write(_get_struct_2d().pack(*self.aux.angle_corrections))
      _x = self
      buff.write(_get_struct_2B().pack(_x.aux.enable_motors, _x.aux.use_external_yaw))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.aux is None:
        self.aux = quadrotor_msgs.msg.AuxCommand()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.thrust, _x.roll, _x.pitch, _x.yaw, _x.aux.current_yaw, _x.aux.kf_correction,) = _get_struct_4f2d().unpack(str[start:end])
      start = end
      end += 16
      self.aux.angle_corrections = _get_struct_2d().unpack(str[start:end])
      _x = self
      start = end
      end += 2
      (_x.aux.enable_motors, _x.aux.use_external_yaw,) = _get_struct_2B().unpack(str[start:end])
      self.aux.enable_motors = bool(self.aux.enable_motors)
      self.aux.use_external_yaw = bool(self.aux.use_external_yaw)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4f2d().pack(_x.thrust, _x.roll, _x.pitch, _x.yaw, _x.aux.current_yaw, _x.aux.kf_correction))
      buff.write(self.aux.angle_corrections.tostring())
      _x = self
      buff.write(_get_struct_2B().pack(_x.aux.enable_motors, _x.aux.use_external_yaw))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.aux is None:
        self.aux = quadrotor_msgs.msg.AuxCommand()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.thrust, _x.roll, _x.pitch, _x.yaw, _x.aux.current_yaw, _x.aux.kf_correction,) = _get_struct_4f2d().unpack(str[start:end])
      start = end
      end += 16
      self.aux.angle_corrections = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=2)
      _x = self
      start = end
      end += 2
      (_x.aux.enable_motors, _x.aux.use_external_yaw,) = _get_struct_2B().unpack(str[start:end])
      self.aux.enable_motors = bool(self.aux.enable_motors)
      self.aux.use_external_yaw = bool(self.aux.use_external_yaw)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4f2d = None
def _get_struct_4f2d():
    global _struct_4f2d
    if _struct_4f2d is None:
        _struct_4f2d = struct.Struct("<4f2d")
    return _struct_4f2d
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B