#!/usr/bin/env python
#
# Copyright 2007 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database


_sym_db = _symbol_database.Default()


from google.appengine.datastore import action_pb2 as google_dot_appengine_dot_datastore_dot_action__pb2
from google.appengine.datastore import entity_bytes_pb2 as google_dot_appengine_dot_datastore_dot_entity__bytes__pb2
from google.appengine.datastore import snapshot_pb2 as google_dot_appengine_dot_datastore_dot_snapshot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/appengine/datastore/datastore_v3_bytes.proto\x12\x1d\x61pphosting_datastore_v3_bytes\x1a\'google/appengine/datastore/action.proto\x1a-google/appengine/datastore/entity_bytes.proto\x1a)google/appengine/datastore/snapshot.proto\"\xa0\x01\n\x0bTransaction\x12\x0e\n\x06handle\x18\x01 \x02(\x06\x12\x0b\n\x03\x61pp\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x06 \x01(\t\x12\x1b\n\x0cmark_changes\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x42\n\x0f\x63omposite_index\x18\x05 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\"\xe1\x0c\n\x05Query\x12\x0b\n\x03\x61pp\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x61tabase_id\x18* \x01(\t\x12\x12\n\nname_space\x18\x1d \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12\x36\n\x08\x61ncestor\x18\x11 \x01(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x0f\n\x07shallow\x18+ \x01(\x08\x12;\n\x06\x66ilter\x18\x04 \x03(\n2+.apphosting_datastore_v3_bytes.Query.Filter\x12\x39\n\x05order\x18\t \x03(\n2*.apphosting_datastore_v3_bytes.Query.Order\x12\r\n\x05\x63ount\x18\x17 \x01(\x05\x12\x11\n\x06offset\x18\x0c \x01(\x05:\x01\x30\x12\r\n\x05limit\x18\x10 \x01(\x05\x12\x46\n\x0f\x63ompiled_cursor\x18\x1e \x01(\x0b\x32-.apphosting_datastore_v3_bytes.CompiledCursor\x12J\n\x13\x65nd_compiled_cursor\x18\x1f \x01(\x0b\x32-.apphosting_datastore_v3_bytes.CompiledCursor\x12\x42\n\x0f\x63omposite_index\x18\x13 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\x12\x18\n\tkeys_only\x18\x15 \x01(\x08:\x05\x66\x61lse\x12?\n\x0btransaction\x18\x16 \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12\x13\n\x0b\x66\x61ilover_ms\x18\x1a \x01(\x03\x12\x0e\n\x06strong\x18  \x01(\x08\x12\x15\n\rproperty_name\x18! \x03(\t\x12\x1e\n\x16group_by_property_name\x18\" \x03(\t\x12\x10\n\x08\x64istinct\x18\x18 \x01(\x08\x12\x1d\n\x15min_safe_time_seconds\x18# \x01(\x03\x12\x19\n\x11safe_replica_name\x18$ \x03(\t\x12\x18\n\x0cread_time_us\x18, \x01(\x03\x42\x02\x18\x01\x12\x1e\n\x16read_time_epoch_micros\x18- \x01(\x03\x12;\n\x04hint\x18\x12 \x01(\x0e\x32).apphosting_datastore_v3_bytes.Query.HintB\x02\x18\x01\x12\x18\n\x0csearch_query\x18\x08 \x01(\tB\x02\x18\x01\x12\'\n\x14require_perfect_plan\x18\x14 \x01(\x08:\x05\x66\x61lseB\x02\x18\x01\x12\x1a\n\x07\x63ompile\x18\x19 \x01(\x08:\x05\x66\x61lseB\x02\x18\x01\x12 \n\x0epersist_offset\x18% \x01(\x08:\x04trueB\x02\x18\x01\x1a\xf3\x02\n\x06\x46ilter\x12@\n\x02op\x18\x06 \x02(\x0e\x32\x34.apphosting_datastore_v3_bytes.Query.Filter.Operator\x12\x35\n\x08property\x18\x0e \x03(\x0b\x32#.storage_onestore_v3_bytes.Property\x12<\n\ngeo_region\x18( \x01(\x0b\x32(.apphosting_datastore_v3_bytes.GeoRegion\"\xb1\x01\n\x08Operator\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05\x45QUAL\x10\x05\x12\x06\n\x02IN\x10\x06\x12\n\n\x06\x45XISTS\x10\x07\x12\x17\n\x13\x43ONTAINED_IN_REGION\x10\x08\x12\r\n\tNOT_EQUAL\x10\t\x12\n\n\x06NOT_IN\x10\n\x1a\x99\x01\n\x05Order\x12\x10\n\x08property\x18\n \x02(\t\x12R\n\tdirection\x18\x0b \x01(\x0e\x32\x34.apphosting_datastore_v3_bytes.Query.Order.Direction:\tASCENDING\"*\n\tDirection\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"=\n\x04Hint\x12\x0f\n\x0bORDER_FIRST\x10\x01\x12\x12\n\x0e\x41NCESTOR_FIRST\x10\x02\x12\x10\n\x0c\x46ILTER_FIRST\x10\x03\"2\n\x0bRegionPoint\x12\x10\n\x08latitude\x18\x01 \x02(\x01\x12\x11\n\tlongitude\x18\x02 \x02(\x01\"a\n\x0c\x43ircleRegion\x12:\n\x06\x63\x65nter\x18\x01 \x02(\x0b\x32*.apphosting_datastore_v3_bytes.RegionPoint\x12\x15\n\rradius_meters\x18\x02 \x02(\x01\"\x8f\x01\n\x0fRectangleRegion\x12=\n\tsouthwest\x18\x01 \x02(\x0b\x32*.apphosting_datastore_v3_bytes.RegionPoint\x12=\n\tnortheast\x18\x02 \x02(\x0b\x32*.apphosting_datastore_v3_bytes.RegionPoint\"\x8b\x01\n\tGeoRegion\x12;\n\x06\x63ircle\x18\x01 \x01(\x0b\x32+.apphosting_datastore_v3_bytes.CircleRegion\x12\x41\n\trectangle\x18\x02 \x01(\x0b\x32..apphosting_datastore_v3_bytes.RectangleRegion\"\xec\x06\n\rCompiledQuery\x12M\n\x0bprimaryscan\x18\x01 \x02(\n28.apphosting_datastore_v3_bytes.CompiledQuery.PrimaryScan\x12Q\n\rmergejoinscan\x18\x07 \x03(\n2:.apphosting_datastore_v3_bytes.CompiledQuery.MergeJoinScan\x12\x33\n\tindex_def\x18\x15 \x01(\x0b\x32 .storage_onestore_v3_bytes.Index\x12\x11\n\x06offset\x18\n \x01(\x05:\x01\x30\x12\r\n\x05limit\x18\x0b \x01(\x05\x12\x11\n\tkeys_only\x18\x0c \x02(\x08\x12\x15\n\rproperty_name\x18\x18 \x03(\t\x12\x1b\n\x13\x64istinct_infix_size\x18\x19 \x01(\x05\x12\x17\n\x0fkey_path_length\x18\x1b \x01(\x05\x12O\n\x0c\x65ntityfilter\x18\r \x01(\n29.apphosting_datastore_v3_bytes.CompiledQuery.EntityFilter\x12\x12\n\nplan_label\x18\x1a \x01(\t\x1a\xd5\x01\n\x0bPrimaryScan\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x11\n\tstart_key\x18\x03 \x01(\x0c\x12\x17\n\x0fstart_inclusive\x18\x04 \x01(\x08\x12\x0f\n\x07\x65nd_key\x18\x05 \x01(\x0c\x12\x15\n\rend_inclusive\x18\x06 \x01(\x08\x12\x1b\n\x13start_postfix_value\x18\x16 \x03(\x0c\x12\x19\n\x11\x65nd_postfix_value\x18\x17 \x03(\x0c\x12&\n\x1e\x65nd_unapplied_log_timestamp_us\x18\x13 \x01(\x03\x1aV\n\rMergeJoinScan\x12\x12\n\nindex_name\x18\x08 \x02(\t\x12\x14\n\x0cprefix_value\x18\t \x03(\x0c\x12\x1b\n\x0cvalue_prefix\x18\x14 \x01(\x08:\x05\x66\x61lse\x1am\n\x0c\x45ntityFilter\x12\x17\n\x08\x64istinct\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x0c\n\x04kind\x18\x11 \x01(\t\x12\x36\n\x08\x61ncestor\x18\x12 \x01(\x0b\x32$.storage_onestore_v3_bytes.Reference\"\xbe\x04\n\x0e\x43ompiledCursor\x12L\n\x08position\x18\x02 \x01(\n26.apphosting_datastore_v3_bytes.CompiledCursor.PositionB\x02\x18\x01\x12\x41\n\x10postfix_position\x18\x01 \x01(\x0b\x32\'.storage_onestore_v3_bytes.IndexPostfix\x12\x43\n\x11\x61\x62solute_position\x18\x03 \x01(\x0b\x32(.storage_onestore_v3_bytes.IndexPosition\x1a\xd5\x02\n\x08Position\x12\x15\n\tstart_key\x18\x1b \x01(\x0c\x42\x02\x18\x01\x12Y\n\nindexvalue\x18\x1d \x03(\n2A.apphosting_datastore_v3_bytes.CompiledCursor.Position.IndexValueB\x02\x18\x01\x12\x35\n\x03key\x18  \x01(\x0b\x32$.storage_onestore_v3_bytes.ReferenceB\x02\x18\x01\x12!\n\x0fstart_inclusive\x18\x1c \x01(\x08:\x04trueB\x02\x18\x01\x12\x1c\n\x10\x62\x65\x66ore_ascending\x18! \x01(\x08\x42\x02\x18\x01\x1a_\n\nIndexValue\x12\x14\n\x08property\x18\x1e \x01(\tB\x02\x18\x01\x12;\n\x05value\x18\x1f \x02(\x0b\x32(.storage_onestore_v3_bytes.PropertyValueB\x02\x18\x01\":\n\x06\x43ursor\x12\x0e\n\x06\x63ursor\x18\x01 \x02(\x06\x12\x0b\n\x03\x61pp\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x03 \x01(\t\"\x9f\x03\n\x05\x45rror\"\x95\x03\n\tErrorCode\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x01\x12\x1a\n\x16\x43ONCURRENT_TRANSACTION\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x0e\n\nNEED_INDEX\x10\x04\x12\x0b\n\x07TIMEOUT\x10\x05\x12\x15\n\x11PERMISSION_DENIED\x10\x06\x12\x12\n\x0e\x42IGTABLE_ERROR\x10\x07\x12 \n\x1c\x43OMMITTED_BUT_STILL_APPLYING\x10\x08\x12\x17\n\x13\x43\x41PABILITY_DISABLED\x10\t\x12\x19\n\x15TRY_ALTERNATE_BACKEND\x10\n\x12\x15\n\x11SAFE_TIME_TOO_OLD\x10\x0b\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x0c\x12\x1c\n\x18SNAPSHOT_VERSION_TOO_OLD\x10\x12\x12\r\n\tNOT_FOUND\x10\r\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x0e\x12\x17\n\x13\x46\x41ILED_PRECONDITION\x10\x0f\x12\x13\n\x0fUNAUTHENTICATED\x10\x10\x12\x0b\n\x07\x41\x42ORTED\x10\x11\"\xbd\x02\n\x04\x43ost\x12\x14\n\x0cindex_writes\x18\x01 \x01(\x05\x12\x19\n\x11index_write_bytes\x18\x02 \x01(\x05\x12\x15\n\rentity_writes\x18\x03 \x01(\x05\x12\x1a\n\x12\x65ntity_write_bytes\x18\x04 \x01(\x05\x12\x42\n\ncommitcost\x18\x05 \x01(\n2..apphosting_datastore_v3_bytes.Cost.CommitCost\x12!\n\x19\x61pproximate_storage_delta\x18\x08 \x01(\x05\x12\x1b\n\x13id_sequence_updates\x18\t \x01(\x05\x1aM\n\nCommitCost\x12\x1d\n\x15requested_entity_puts\x18\x06 \x01(\x05\x12 \n\x18requested_entity_deletes\x18\x07 \x01(\x05\"\xe8\x01\n\nGetRequest\x12\x31\n\x03key\x18\x01 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12?\n\x0btransaction\x18\x02 \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12\x0e\n\x06strong\x18\x04 \x01(\x08\x12\x1d\n\x0e\x61llow_deferred\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x16read_time_epoch_micros\x18\x06 \x01(\x03\x12\x17\n\x0b\x66\x61ilover_ms\x18\x03 \x01(\x03\x42\x02\x18\x01\"\xe9\x02\n\x0bGetResponse\x12\x41\n\x06\x65ntity\x18\x01 \x03(\n21.apphosting_datastore_v3_bytes.GetResponse.Entity\x12\x36\n\x08\x64\x65\x66\x65rred\x18\x05 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x16\n\x08in_order\x18\x06 \x01(\x08:\x04true\x12\x1e\n\x16read_time_epoch_micros\x18\x07 \x01(\x03\x1a\xa6\x01\n\x06\x45ntity\x12\x36\n\x06\x65ntity\x18\x02 \x01(\x0b\x32&.storage_onestore_v3_bytes.EntityProto\x12\x31\n\x03key\x18\x04 \x01(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12 \n\x18update_time_epoch_micros\x18\x08 \x01(\x03\"\xe4\x03\n\nPutRequest\x12\x36\n\x06\x65ntity\x18\x01 \x03(\x0b\x32&.storage_onestore_v3_bytes.EntityProto\x12?\n\x0btransaction\x18\x02 \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12\x42\n\x0f\x63omposite_index\x18\x03 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\x12\x16\n\x07trusted\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05\x66orce\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cmark_changes\x18\x08 \x01(\x08:\x05\x66\x61lse\x12/\n\x08snapshot\x18\t \x03(\x0b\x32\x1d.storage_onestore_v3.Snapshot\x12W\n\x0e\x61uto_id_policy\x18\n \x01(\x0e\x32\x36.apphosting_datastore_v3_bytes.PutRequest.AutoIdPolicy:\x07\x43URRENT\x12\x17\n\x0fsequence_number\x18\x0c \x01(\x03\"+\n\x0c\x41utoIdPolicy\x12\x0b\n\x07\x43URRENT\x10\x00\x12\x0e\n\nSEQUENTIAL\x10\x01\"\xa6\x01\n\x0bPutResponse\x12\x31\n\x03key\x18\x01 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x31\n\x04\x63ost\x18\x02 \x01(\x0b\x32#.apphosting_datastore_v3_bytes.Cost\x12\x0f\n\x07version\x18\x03 \x03(\x03\x12 \n\x18update_time_epoch_micros\x18\x04 \x03(\x03\"\xcc\x01\n\x0cTouchRequest\x12\x31\n\x03key\x18\x01 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x42\n\x0f\x63omposite_index\x18\x02 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\x12\x14\n\x05\x66orce\x18\x03 \x01(\x08:\x05\x66\x61lse\x12/\n\x08snapshot\x18\t \x03(\x0b\x32\x1d.storage_onestore_v3.Snapshot\"B\n\rTouchResponse\x12\x31\n\x04\x63ost\x18\x01 \x01(\x0b\x32#.apphosting_datastore_v3_bytes.Cost\"\xdc\x02\n\rDeleteRequest\x12\x31\n\x03key\x18\x06 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12?\n\x0btransaction\x18\x05 \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12\x42\n\x0f\x63omposite_index\x18\x0b \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\x12\x16\n\x07trusted\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05\x66orce\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cmark_changes\x18\x08 \x01(\x08:\x05\x66\x61lse\x12/\n\x08snapshot\x18\t \x03(\x0b\x32\x1d.storage_onestore_v3.Snapshot\x12\x17\n\x0fsequence_number\x18\x0c \x01(\x03\"v\n\x0e\x44\x65leteResponse\x12\x31\n\x04\x63ost\x18\x01 \x01(\x0b\x32#.apphosting_datastore_v3_bytes.Cost\x12\x0f\n\x07version\x18\x03 \x03(\x03\x12 \n\x18\x64\x65lete_time_epoch_micros\x18\x04 \x03(\x03\"\x82\x01\n\x0bNextRequest\x12\x35\n\x06\x63ursor\x18\x01 \x02(\x0b\x32%.apphosting_datastore_v3_bytes.Cursor\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x15\n\x06offset\x18\x04 \x01(\x05:\x01\x30\x42\x02\x18\x01\x12\x16\n\x07\x63ompile\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xa7\x05\n\x0bQueryResult\x12\x35\n\x06\x63ursor\x18\x01 \x01(\x0b\x32%.apphosting_datastore_v3_bytes.Cursor\x12\x36\n\x06result\x18\x02 \x03(\x0b\x32&.storage_onestore_v3_bytes.EntityProto\x12\x17\n\x0fskipped_results\x18\x07 \x01(\x05\x12\x14\n\x0cmore_results\x18\x03 \x02(\x08\x12\x11\n\tkeys_only\x18\x04 \x01(\x08\x12\x12\n\nindex_only\x18\t \x01(\x08\x12\x11\n\tsmall_ops\x18\n \x01(\x08\x12\x44\n\x0e\x63ompiled_query\x18\x05 \x01(\x0b\x32,.apphosting_datastore_v3_bytes.CompiledQuery\x12\x46\n\x0f\x63ompiled_cursor\x18\x06 \x01(\x0b\x32-.apphosting_datastore_v3_bytes.CompiledCursor\x12\x38\n\x05index\x18\x08 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\x12\x0f\n\x07version\x18\x0b \x03(\x03\x12 \n\x18update_time_epoch_micros\x18\x0f \x03(\x03\x12\x1e\n\x16read_time_epoch_micros\x18\x0e \x01(\x03\x12M\n\x16result_compiled_cursor\x18\x0c \x03(\x0b\x32-.apphosting_datastore_v3_bytes.CompiledCursor\x12V\n\x1fskipped_results_compiled_cursor\x18\r \x01(\x0b\x32-.apphosting_datastore_v3_bytes.CompiledCursor\"\xb7\x01\n\x12\x41llocateIdsRequest\x12\x37\n\tmodel_key\x18\x01 \x01(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0b\n\x03max\x18\x03 \x01(\x03\x12\x35\n\x07reserve\x18\x05 \x03(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x16\n\x07trusted\x18\x06 \x01(\x08:\x05\x66\x61lse\"d\n\x13\x41llocateIdsResponse\x12\r\n\x05start\x18\x01 \x02(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x02(\x03\x12\x31\n\x04\x63ost\x18\x03 \x01(\x0b\x32#.apphosting_datastore_v3_bytes.Cost\"L\n\x10\x43ompositeIndices\x12\x38\n\x05index\x18\x01 \x03(\x0b\x32).storage_onestore_v3_bytes.CompositeIndex\"\x81\x01\n\x11\x41\x64\x64\x41\x63tionsRequest\x12?\n\x0btransaction\x18\x01 \x02(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\x12+\n\x06\x61\x63tion\x18\x02 \x03(\x0b\x32\x1b.storage_onestore_v3.Action\"\x14\n\x12\x41\x64\x64\x41\x63tionsResponse\"\xc5\x02\n\x17\x42\x65ginTransactionRequest\x12\x0b\n\x03\x61pp\x18\x01 \x02(\t\x12 \n\x11\x61llow_multiple_eg\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0b\x64\x61tabase_id\x18\x04 \x01(\t\x12]\n\x04mode\x18\x05 \x01(\x0e\x32\x46.apphosting_datastore_v3_bytes.BeginTransactionRequest.TransactionMode:\x07UNKNOWN\x12H\n\x14previous_transaction\x18\x07 \x01(\x0b\x32*.apphosting_datastore_v3_bytes.Transaction\"=\n\x0fTransactionMode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\"\xaa\x02\n\x0e\x43ommitResponse\x12\x31\n\x04\x63ost\x18\x01 \x01(\x0b\x32#.apphosting_datastore_v3_bytes.Cost\x12 \n\x18\x63ommit_time_epoch_micros\x18\x07 \x01(\x03\x12\x46\n\x07version\x18\x03 \x03(\n25.apphosting_datastore_v3_bytes.CommitResponse.Version\x1a{\n\x07Version\x12=\n\x0froot_entity_key\x18\x04 \x02(\x0b\x32$.storage_onestore_v3_bytes.Reference\x12\x0f\n\x07version\x18\x05 \x02(\x03\x12 \n\x18update_time_epoch_micros\x18\x06 \x01(\x03\"8\n\x11GetIndicesRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x02 \x01(\t\"6\n\x13UpdateIndexResponse\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x86\x02\n\x12\x44\x61tastoreService_3\"\xef\x01\n\x06Method\x12\x07\n\x03Get\x10\x01\x12\x07\n\x03Put\x10\x02\x12\t\n\x05Touch\x10\x03\x12\n\n\x06\x44\x65lete\x10\x04\x12\x0c\n\x08RunQuery\x10\x05\x12\x0e\n\nAddActions\x10\x06\x12\x08\n\x04Next\x10\x07\x12\x10\n\x0c\x44\x65leteCursor\x10\x08\x12\x14\n\x10\x42\x65ginTransaction\x10\t\x12\n\n\x06\x43ommit\x10\n\x12\x0c\n\x08Rollback\x10\x0b\x12\x0f\n\x0b\x41llocateIds\x10\x0c\x12\x0f\n\x0b\x43reateIndex\x10\r\x12\x0f\n\x0bUpdateIndex\x10\x0e\x12\x0e\n\nGetIndices\x10\x0f\x12\x0f\n\x0b\x44\x65leteIndex\x10\x10\x42\x36\n%com.google.google.appengine.datastoreB\rDatastoreV3Pb')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.datastore.datastore_v3_bytes_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.google.appengine.datastoreB\rDatastoreV3Pb'
  _QUERY.fields_by_name['read_time_us']._options = None
  _QUERY.fields_by_name['read_time_us']._serialized_options = b'\030\001'
  _QUERY.fields_by_name['hint']._options = None
  _QUERY.fields_by_name['hint']._serialized_options = b'\030\001'
  _QUERY.fields_by_name['search_query']._options = None
  _QUERY.fields_by_name['search_query']._serialized_options = b'\030\001'
  _QUERY.fields_by_name['require_perfect_plan']._options = None
  _QUERY.fields_by_name['require_perfect_plan']._serialized_options = b'\030\001'
  _QUERY.fields_by_name['compile']._options = None
  _QUERY.fields_by_name['compile']._serialized_options = b'\030\001'
  _QUERY.fields_by_name['persist_offset']._options = None
  _QUERY.fields_by_name['persist_offset']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION_INDEXVALUE.fields_by_name['property']._options = None
  _COMPILEDCURSOR_POSITION_INDEXVALUE.fields_by_name['property']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION_INDEXVALUE.fields_by_name['value']._options = None
  _COMPILEDCURSOR_POSITION_INDEXVALUE.fields_by_name['value']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION.fields_by_name['start_key']._options = None
  _COMPILEDCURSOR_POSITION.fields_by_name['start_key']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION.fields_by_name['indexvalue']._options = None
  _COMPILEDCURSOR_POSITION.fields_by_name['indexvalue']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION.fields_by_name['key']._options = None
  _COMPILEDCURSOR_POSITION.fields_by_name['key']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION.fields_by_name['start_inclusive']._options = None
  _COMPILEDCURSOR_POSITION.fields_by_name['start_inclusive']._serialized_options = b'\030\001'
  _COMPILEDCURSOR_POSITION.fields_by_name['before_ascending']._options = None
  _COMPILEDCURSOR_POSITION.fields_by_name['before_ascending']._serialized_options = b'\030\001'
  _COMPILEDCURSOR.fields_by_name['position']._options = None
  _COMPILEDCURSOR.fields_by_name['position']._serialized_options = b'\030\001'
  _GETREQUEST.fields_by_name['failover_ms']._options = None
  _GETREQUEST.fields_by_name['failover_ms']._serialized_options = b'\030\001'
  _NEXTREQUEST.fields_by_name['offset']._options = None
  _NEXTREQUEST.fields_by_name['offset']._serialized_options = b'\030\001'
  _TRANSACTION._serialized_start=218
  _TRANSACTION._serialized_end=378
  _QUERY._serialized_start=381
  _QUERY._serialized_end=2014
  _QUERY_FILTER._serialized_start=1424
  _QUERY_FILTER._serialized_end=1795
  _QUERY_FILTER_OPERATOR._serialized_start=1618
  _QUERY_FILTER_OPERATOR._serialized_end=1795
  _QUERY_ORDER._serialized_start=1798
  _QUERY_ORDER._serialized_end=1951
  _QUERY_ORDER_DIRECTION._serialized_start=1909
  _QUERY_ORDER_DIRECTION._serialized_end=1951
  _QUERY_HINT._serialized_start=1953
  _QUERY_HINT._serialized_end=2014
  _REGIONPOINT._serialized_start=2016
  _REGIONPOINT._serialized_end=2066
  _CIRCLEREGION._serialized_start=2068
  _CIRCLEREGION._serialized_end=2165
  _RECTANGLEREGION._serialized_start=2168
  _RECTANGLEREGION._serialized_end=2311
  _GEOREGION._serialized_start=2314
  _GEOREGION._serialized_end=2453
  _COMPILEDQUERY._serialized_start=2456
  _COMPILEDQUERY._serialized_end=3332
  _COMPILEDQUERY_PRIMARYSCAN._serialized_start=2920
  _COMPILEDQUERY_PRIMARYSCAN._serialized_end=3133
  _COMPILEDQUERY_MERGEJOINSCAN._serialized_start=3135
  _COMPILEDQUERY_MERGEJOINSCAN._serialized_end=3221
  _COMPILEDQUERY_ENTITYFILTER._serialized_start=3223
  _COMPILEDQUERY_ENTITYFILTER._serialized_end=3332
  _COMPILEDCURSOR._serialized_start=3335
  _COMPILEDCURSOR._serialized_end=3909
  _COMPILEDCURSOR_POSITION._serialized_start=3568
  _COMPILEDCURSOR_POSITION._serialized_end=3909
  _COMPILEDCURSOR_POSITION_INDEXVALUE._serialized_start=3814
  _COMPILEDCURSOR_POSITION_INDEXVALUE._serialized_end=3909
  _CURSOR._serialized_start=3911
  _CURSOR._serialized_end=3969
  _ERROR._serialized_start=3972
  _ERROR._serialized_end=4387
  _ERROR_ERRORCODE._serialized_start=3982
  _ERROR_ERRORCODE._serialized_end=4387
  _COST._serialized_start=4390
  _COST._serialized_end=4707
  _COST_COMMITCOST._serialized_start=4630
  _COST_COMMITCOST._serialized_end=4707
  _GETREQUEST._serialized_start=4710
  _GETREQUEST._serialized_end=4942
  _GETRESPONSE._serialized_start=4945
  _GETRESPONSE._serialized_end=5306
  _GETRESPONSE_ENTITY._serialized_start=5140
  _GETRESPONSE_ENTITY._serialized_end=5306
  _PUTREQUEST._serialized_start=5309
  _PUTREQUEST._serialized_end=5793
  _PUTREQUEST_AUTOIDPOLICY._serialized_start=5750
  _PUTREQUEST_AUTOIDPOLICY._serialized_end=5793
  _PUTRESPONSE._serialized_start=5796
  _PUTRESPONSE._serialized_end=5962
  _TOUCHREQUEST._serialized_start=5965
  _TOUCHREQUEST._serialized_end=6169
  _TOUCHRESPONSE._serialized_start=6171
  _TOUCHRESPONSE._serialized_end=6237
  _DELETEREQUEST._serialized_start=6240
  _DELETEREQUEST._serialized_end=6588
  _DELETERESPONSE._serialized_start=6590
  _DELETERESPONSE._serialized_end=6708
  _NEXTREQUEST._serialized_start=6711
  _NEXTREQUEST._serialized_end=6841
  _QUERYRESULT._serialized_start=6844
  _QUERYRESULT._serialized_end=7523
  _ALLOCATEIDSREQUEST._serialized_start=7526
  _ALLOCATEIDSREQUEST._serialized_end=7709
  _ALLOCATEIDSRESPONSE._serialized_start=7711
  _ALLOCATEIDSRESPONSE._serialized_end=7811
  _COMPOSITEINDICES._serialized_start=7813
  _COMPOSITEINDICES._serialized_end=7889
  _ADDACTIONSREQUEST._serialized_start=7892
  _ADDACTIONSREQUEST._serialized_end=8021
  _ADDACTIONSRESPONSE._serialized_start=8023
  _ADDACTIONSRESPONSE._serialized_end=8043
  _BEGINTRANSACTIONREQUEST._serialized_start=8046
  _BEGINTRANSACTIONREQUEST._serialized_end=8371
  _BEGINTRANSACTIONREQUEST_TRANSACTIONMODE._serialized_start=8310
  _BEGINTRANSACTIONREQUEST_TRANSACTIONMODE._serialized_end=8371
  _COMMITRESPONSE._serialized_start=8374
  _COMMITRESPONSE._serialized_end=8672
  _COMMITRESPONSE_VERSION._serialized_start=8549
  _COMMITRESPONSE_VERSION._serialized_end=8672
  _GETINDICESREQUEST._serialized_start=8674
  _GETINDICESREQUEST._serialized_end=8730
  _UPDATEINDEXRESPONSE._serialized_start=8732
  _UPDATEINDEXRESPONSE._serialized_end=8786
  _DATASTORESERVICE_3._serialized_start=8789
  _DATASTORESERVICE_3._serialized_end=9051
  _DATASTORESERVICE_3_METHOD._serialized_start=8812
  _DATASTORESERVICE_3_METHOD._serialized_end=9051

