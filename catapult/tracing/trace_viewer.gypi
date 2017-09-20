# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'tracing_css_files': [
      'tracing/ui/base/list_view.css',
      'tracing/ui/extras/about_tracing/common.css',
      'tracing/ui/extras/chrome/cc/display_item_list_view.css',
      'tracing/ui/extras/chrome/cc/layer_picker.css',
      'tracing/ui/extras/chrome/cc/layer_tree_host_impl_view.css',
      'tracing/ui/extras/chrome/cc/layer_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_summary_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_list_view.css',
      'tracing/ui/extras/chrome/cc/picture_view.css',
      'tracing/ui/extras/chrome/gpu/state_view.css',
      'tracing/ui/extras/system_stats/system_stats_instance_track.css',
      'tracing/ui/extras/system_stats/system_stats_snapshot_view.css',
      'tracing/ui/tracks/drawing_container.css',
      'tracing/ui/tracks/object_instance_track.css',
      'tracing/ui/tracks/process_track_base.css',
      'tracing/ui/tracks/rect_track.css',
      'tracing/ui/tracks/spacing_track.css',
      'tracing/ui/tracks/thread_track.css',
      'tracing/ui/tracks/track.css',
    ],
    'tracing_js_html_files': [
      '../third_party/polymer/components/polymer/polymer-micro.html',
      '../third_party/polymer/components/polymer/polymer-mini.html',
      '../third_party/polymer/components/polymer/polymer.html',
      'tracing/base/base.html',
      'tracing/base/base64.html',
      'tracing/base/category_util.html',
      'tracing/base/color.html',
      'tracing/base/color_scheme.html',
      'tracing/base/event.html',
      'tracing/base/event_target.html',
      'tracing/base/extension_registry.html',
      'tracing/base/extension_registry_base.html',
      'tracing/base/extension_registry_basic.html',
      'tracing/base/extension_registry_type_based.html',
      'tracing/base/fixed_color_scheme.html',
      'tracing/base/guid.html',
      'tracing/base/in_memory_trace_stream.html',
      'tracing/base/interval_tree.html',
      'tracing/base/math/bbox2.html',
      'tracing/base/math/math.html',
      'tracing/base/math/piecewise_linear_function.html',
      'tracing/base/math/quad.html',
      'tracing/base/math/range.html',
      'tracing/base/math/range_utils.html',
      'tracing/base/math/rect.html',
      'tracing/base/math/running_statistics.html',
      'tracing/base/math/statistics.html',
      'tracing/base/multi_dimensional_view.html',
      'tracing/base/raf.html',
      'tracing/base/scalar.html',
      'tracing/base/serializable.html',
      'tracing/base/settings.html',
      'tracing/base/sinebow_color_generator.html',
      'tracing/base/task.html',
      'tracing/base/time_display_modes.html',
      'tracing/base/timing.html',
      'tracing/base/trace_stream.html',
      'tracing/base/unit.html',
      'tracing/base/unit_scale.html',
      'tracing/base/utils.html',
      'tracing/base/view_state.html',
      'tracing/core/auditor.html',
      'tracing/core/filter.html',
      'tracing/core/scripting_controller.html',
      'tracing/core/scripting_object.html',
      'tracing/extras/android/android_auditor.html',
      'tracing/extras/chrome/blame_context/blame_context.html',
      'tracing/extras/chrome/blame_context/frame_tree_node.html',
      'tracing/extras/chrome/blame_context/render_frame.html',
      'tracing/extras/chrome/blame_context/top_level.html',
      'tracing/extras/chrome/cc/cc.html',
      'tracing/extras/chrome/cc/constants.html',
      'tracing/extras/chrome/cc/debug_colors.html',
      'tracing/extras/chrome/cc/display_item_list.html',
      'tracing/extras/chrome/cc/input_latency_async_slice.html',
      'tracing/extras/chrome/cc/layer_impl.html',
      'tracing/extras/chrome/cc/layer_tree_host_impl.html',
      'tracing/extras/chrome/cc/layer_tree_impl.html',
      'tracing/extras/chrome/cc/picture.html',
      'tracing/extras/chrome/cc/picture_as_image_data.html',
      'tracing/extras/chrome/cc/raster_task.html',
      'tracing/extras/chrome/cc/region.html',
      'tracing/extras/chrome/cc/render_pass.html',
      'tracing/extras/chrome/cc/tile.html',
      'tracing/extras/chrome/cc/tile_coverage_rect.html',
      'tracing/extras/chrome/cc/util.html',
      'tracing/extras/chrome/chrome_auditor.html',
      'tracing/extras/chrome/chrome_processes.html',
      'tracing/extras/chrome/chrome_user_friendly_category_driver.html',
      'tracing/extras/chrome/cpu_time.html',
      'tracing/extras/chrome/estimated_input_latency.html',
      'tracing/extras/chrome/gpu/gpu_async_slice.html',
      'tracing/extras/chrome/gpu/state.html',
      'tracing/extras/chrome/layout_object.html',
      'tracing/extras/chrome/layout_tree.html',
      'tracing/extras/chrome_config.html',
      'tracing/extras/cpu/cpu_usage_auditor.html',
      'tracing/extras/importer/android/atrace_process_dump_importer.html',
      'tracing/extras/importer/android/event_log_importer.html',
      'tracing/extras/importer/android/process_data_importer.html',
      'tracing/extras/importer/battor_importer.html',
      'tracing/extras/importer/ddms_importer.html',
      'tracing/extras/importer/etw/etw_importer.html',
      'tracing/extras/importer/etw/eventtrace_parser.html',
      'tracing/extras/importer/etw/parser.html',
      'tracing/extras/importer/etw/process_parser.html',
      'tracing/extras/importer/etw/thread_parser.html',
      'tracing/extras/importer/fuchsia_importer.html',
      'tracing/extras/importer/gcloud_trace/gcloud_trace_importer.html',
      'tracing/extras/importer/gzip_importer.html',
      'tracing/extras/importer/heap_dump_trace_event_importer.html',
      'tracing/extras/importer/jszip.html',
      'tracing/extras/importer/legacy_heap_dump_trace_event_importer.html',
      'tracing/extras/importer/linux_perf/android_parser.html',
      'tracing/extras/importer/linux_perf/binder_parser.html',
      'tracing/extras/importer/linux_perf/bus_parser.html',
      'tracing/extras/importer/linux_perf/clock_parser.html',
      'tracing/extras/importer/linux_perf/cpufreq_parser.html',
      'tracing/extras/importer/linux_perf/disk_parser.html',
      'tracing/extras/importer/linux_perf/drm_parser.html',
      'tracing/extras/importer/linux_perf/exynos_parser.html',
      'tracing/extras/importer/linux_perf/ftrace_importer.html',
      'tracing/extras/importer/linux_perf/gesture_parser.html',
      'tracing/extras/importer/linux_perf/i2c_parser.html',
      'tracing/extras/importer/linux_perf/i915_parser.html',
      'tracing/extras/importer/linux_perf/irq_parser.html',
      'tracing/extras/importer/linux_perf/kfunc_parser.html',
      'tracing/extras/importer/linux_perf/mali_parser.html',
      'tracing/extras/importer/linux_perf/memreclaim_parser.html',
      'tracing/extras/importer/linux_perf/parser.html',
      'tracing/extras/importer/linux_perf/power_parser.html',
      'tracing/extras/importer/linux_perf/regulator_parser.html',
      'tracing/extras/importer/linux_perf/sched_parser.html',
      'tracing/extras/importer/linux_perf/sync_parser.html',
      'tracing/extras/importer/linux_perf/workqueue_parser.html',
      'tracing/extras/importer/oboe.html',
      'tracing/extras/importer/profiling_dictionary_reader.html',
      'tracing/extras/importer/trace2html_importer.html',
      'tracing/extras/importer/trace_code_entry.html',
      'tracing/extras/importer/trace_code_map.html',
      'tracing/extras/importer/trace_event_importer.html',
      'tracing/extras/importer/v8/codemap.html',
      'tracing/extras/importer/v8/log_reader.html',
      'tracing/extras/importer/v8/splaytree.html',
      'tracing/extras/importer/v8/v8_log_importer.html',
      'tracing/extras/importer/zip_importer.html',
      'tracing/extras/lean_config.html',
      'tracing/extras/measure/measure.html',
      'tracing/extras/measure/measure_async_slice.html',
      'tracing/extras/memory/lowmemory_auditor.html',
      'tracing/extras/net/net.html',
      'tracing/extras/net/net_async_slice.html',
      'tracing/extras/system_stats/system_stats_snapshot.html',
      'tracing/extras/systrace_config.html',
      'tracing/extras/tquery/context.html',
      'tracing/extras/tquery/filter.html',
      'tracing/extras/tquery/filter_all_of.html',
      'tracing/extras/tquery/filter_any_of.html',
      'tracing/extras/tquery/filter_has_ancestor.html',
      'tracing/extras/tquery/filter_has_duration.html',
      'tracing/extras/tquery/filter_has_title.html',
      'tracing/extras/tquery/filter_is_top_level.html',
      'tracing/extras/tquery/filter_not.html',
      'tracing/extras/tquery/tquery.html',
      'tracing/extras/v8/ic_stats_entry.html',
      'tracing/extras/v8/runtime_stats_entry.html',
      'tracing/extras/v8/v8_cpu_profile_node.html',
      'tracing/extras/v8/v8_gc_stats_thread_slice.html',
      'tracing/extras/v8/v8_ic_stats_thread_slice.html',
      'tracing/extras/v8/v8_thread_slice.html',
      'tracing/extras/v8_config.html',
      'tracing/extras/vsync/vsync_auditor.html',
      'tracing/importer/context_processor.html',
      'tracing/importer/empty_importer.html',
      'tracing/importer/find_input_expectations.html',
      'tracing/importer/find_load_expectations.html',
      'tracing/importer/find_startup_expectations.html',
      'tracing/importer/import.html',
      'tracing/importer/importer.html',
      'tracing/importer/proto_expectation.html',
      'tracing/importer/simple_line_reader.html',
      'tracing/importer/user_model_builder.html',
      'tracing/metrics/all_fixed_color_schemes.html',
      'tracing/metrics/all_metrics.html',
      'tracing/metrics/android_systrace_metric.html',
      'tracing/metrics/blink/gc_metric.html',
      'tracing/metrics/cpu_process_metric.html',
      'tracing/metrics/media_metric.html',
      'tracing/metrics/metric_map_function.html',
      'tracing/metrics/metric_registry.html',
      'tracing/metrics/sample_metric.html',
      'tracing/metrics/spa_navigation_helper.html',
      'tracing/metrics/spa_navigation_metric.html',
      'tracing/metrics/system_health/breakdown_tree_helpers.html',
      'tracing/metrics/system_health/clock_sync_latency_metric.html',
      'tracing/metrics/system_health/cpu_time_metric.html',
      'tracing/metrics/system_health/cpu_time_tree_data_reporter.html',
      'tracing/metrics/system_health/expected_queueing_time_metric.html',
      'tracing/metrics/system_health/loading_metric.html',
      'tracing/metrics/system_health/long_tasks_metric.html',
      'tracing/metrics/system_health/memory_metric.html',
      'tracing/metrics/system_health/new_cpu_time_metric.html',
      'tracing/metrics/system_health/power_metric.html',
      'tracing/metrics/system_health/responsiveness_metric.html',
      'tracing/metrics/system_health/utils.html',
      'tracing/metrics/system_health/webview_startup_metric.html',
      'tracing/metrics/tracing_metric.html',
      'tracing/metrics/v8/execution_metric.html',
      'tracing/metrics/v8/gc_metric.html',
      'tracing/metrics/v8/runtime_stats_metric.html',
      'tracing/metrics/v8/utils.html',
      'tracing/metrics/v8/v8_metrics.html',
      'tracing/metrics/vr/frame_cycle_duration_metric.html',
      'tracing/metrics/vr/webvr_metric.html',
      'tracing/metrics/webrtc/webrtc_rendering_metric.html',
      'tracing/model/activity.html',
      'tracing/model/alert.html',
      'tracing/model/annotation.html',
      'tracing/model/async_slice.html',
      'tracing/model/async_slice_group.html',
      'tracing/model/clock_sync_manager.html',
      'tracing/model/comment_box_annotation.html',
      'tracing/model/compound_event_selection_state.html',
      'tracing/model/constants.html',
      'tracing/model/container_memory_dump.html',
      'tracing/model/counter.html',
      'tracing/model/counter_sample.html',
      'tracing/model/counter_series.html',
      'tracing/model/cpu.html',
      'tracing/model/cpu_slice.html',
      'tracing/model/device.html',
      'tracing/model/event.html',
      'tracing/model/event_container.html',
      'tracing/model/event_info.html',
      'tracing/model/event_registry.html',
      'tracing/model/event_set.html',
      'tracing/model/flow_event.html',
      'tracing/model/frame.html',
      'tracing/model/global_memory_dump.html',
      'tracing/model/heap_dump.html',
      'tracing/model/helpers/android_app.html',
      'tracing/model/helpers/android_model_helper.html',
      'tracing/model/helpers/android_surface_flinger.html',
      'tracing/model/helpers/chrome_browser_helper.html',
      'tracing/model/helpers/chrome_gpu_helper.html',
      'tracing/model/helpers/chrome_model_helper.html',
      'tracing/model/helpers/chrome_process_helper.html',
      'tracing/model/helpers/chrome_renderer_helper.html',
      'tracing/model/helpers/chrome_thread_helper.html',
      'tracing/model/instant_event.html',
      'tracing/model/ir_coverage.html',
      'tracing/model/kernel.html',
      'tracing/model/location.html',
      'tracing/model/memory_allocator_dump.html',
      'tracing/model/model.html',
      'tracing/model/model_indices.html',
      'tracing/model/model_settings.html',
      'tracing/model/model_stats.html',
      'tracing/model/object_collection.html',
      'tracing/model/object_instance.html',
      'tracing/model/object_snapshot.html',
      'tracing/model/power_sample.html',
      'tracing/model/power_series.html',
      'tracing/model/process.html',
      'tracing/model/process_base.html',
      'tracing/model/process_memory_dump.html',
      'tracing/model/profile_node.html',
      'tracing/model/profile_tree.html',
      'tracing/model/proxy_selectable_item.html',
      'tracing/model/rect_annotation.html',
      'tracing/model/resource_usage_sample.html',
      'tracing/model/resource_usage_series.html',
      'tracing/model/sample.html',
      'tracing/model/scoped_id.html',
      'tracing/model/selectable_item.html',
      'tracing/model/selection_state.html',
      'tracing/model/slice.html',
      'tracing/model/slice_group.html',
      'tracing/model/source_info/js_source_info.html',
      'tracing/model/source_info/source_info.html',
      'tracing/model/stack_frame.html',
      'tracing/model/thread.html',
      'tracing/model/thread_slice.html',
      'tracing/model/thread_time_slice.html',
      'tracing/model/time_to_object_instance_map.html',
      'tracing/model/timed_event.html',
      'tracing/model/user_model/animation_expectation.html',
      'tracing/model/user_model/idle_expectation.html',
      'tracing/model/user_model/load_expectation.html',
      'tracing/model/user_model/response_expectation.html',
      'tracing/model/user_model/segment.html',
      'tracing/model/user_model/startup_expectation.html',
      'tracing/model/user_model/user_expectation.html',
      'tracing/model/user_model/user_model.html',
      'tracing/model/vm_region.html',
      'tracing/model/x_marker_annotation.html',
      'tracing/mre/failure.html',
      'tracing/mre/function_handle.html',
      'tracing/mre/mre_result.html',
      'tracing/ui/analysis/alert_sub_view.html',
      'tracing/ui/analysis/analysis_link.html',
      'tracing/ui/analysis/analysis_sub_view.html',
      'tracing/ui/analysis/analysis_view.html',
      'tracing/ui/analysis/container_memory_dump_sub_view.html',
      'tracing/ui/analysis/counter_sample_sub_view.html',
      'tracing/ui/analysis/flow_classifier.html',
      'tracing/ui/analysis/frame_power_usage_chart.html',
      'tracing/ui/analysis/generic_object_view.html',
      'tracing/ui/analysis/memory_dump_allocator_details_pane.html',
      'tracing/ui/analysis/memory_dump_header_pane.html',
      'tracing/ui/analysis/memory_dump_heap_details_breakdown_view.html',
      'tracing/ui/analysis/memory_dump_heap_details_pane.html',
      'tracing/ui/analysis/memory_dump_heap_details_path_view.html',
      'tracing/ui/analysis/memory_dump_heap_details_util.html',
      'tracing/ui/analysis/memory_dump_overview_pane.html',
      'tracing/ui/analysis/memory_dump_sub_view_util.html',
      'tracing/ui/analysis/memory_dump_vm_regions_details_pane.html',
      'tracing/ui/analysis/multi_async_slice_sub_view.html',
      'tracing/ui/analysis/multi_cpu_slice_sub_view.html',
      'tracing/ui/analysis/multi_event_sub_view.html',
      'tracing/ui/analysis/multi_event_summary.html',
      'tracing/ui/analysis/multi_event_summary_table.html',
      'tracing/ui/analysis/multi_flow_event_sub_view.html',
      'tracing/ui/analysis/multi_frame_sub_view.html',
      'tracing/ui/analysis/multi_instant_event_sub_view.html',
      'tracing/ui/analysis/multi_object_sub_view.html',
      'tracing/ui/analysis/multi_power_sample_sub_view.html',
      'tracing/ui/analysis/multi_sample_sub_view.html',
      'tracing/ui/analysis/multi_thread_slice_sub_view.html',
      'tracing/ui/analysis/multi_thread_time_slice_sub_view.html',
      'tracing/ui/analysis/multi_user_expectation_sub_view.html',
      'tracing/ui/analysis/object_instance_view.html',
      'tracing/ui/analysis/object_snapshot_view.html',
      'tracing/ui/analysis/power_sample_summary_table.html',
      'tracing/ui/analysis/rebuildable_behavior.html',
      'tracing/ui/analysis/related_events.html',
      'tracing/ui/analysis/selection_summary_table.html',
      'tracing/ui/analysis/single_async_slice_sub_view.html',
      'tracing/ui/analysis/single_cpu_slice_sub_view.html',
      'tracing/ui/analysis/single_event_sub_view.html',
      'tracing/ui/analysis/single_flow_event_sub_view.html',
      'tracing/ui/analysis/single_frame_sub_view.html',
      'tracing/ui/analysis/single_instant_event_sub_view.html',
      'tracing/ui/analysis/single_object_instance_sub_view.html',
      'tracing/ui/analysis/single_object_snapshot_sub_view.html',
      'tracing/ui/analysis/single_power_sample_sub_view.html',
      'tracing/ui/analysis/single_sample_sub_view.html',
      'tracing/ui/analysis/single_thread_slice_sub_view.html',
      'tracing/ui/analysis/single_thread_time_slice_sub_view.html',
      'tracing/ui/analysis/single_user_expectation_sub_view.html',
      'tracing/ui/analysis/stack_frame.html',
      'tracing/ui/analysis/stacked_pane.html',
      'tracing/ui/analysis/stacked_pane_view.html',
      'tracing/ui/analysis/user_expectation_related_samples_table.html',
      'tracing/ui/annotations/annotation_view.html',
      'tracing/ui/annotations/comment_box_annotation_view.html',
      'tracing/ui/annotations/rect_annotation_view.html',
      'tracing/ui/annotations/x_marker_annotation_view.html',
      'tracing/ui/base/animation.html',
      'tracing/ui/base/animation_controller.html',
      'tracing/ui/base/bar_chart.html',
      'tracing/ui/base/base.html',
      'tracing/ui/base/box_chart.html',
      'tracing/ui/base/camera.html',
      'tracing/ui/base/chart_base.html',
      'tracing/ui/base/chart_base_2d.html',
      'tracing/ui/base/chart_base_2d_brushable_x.html',
      'tracing/ui/base/chart_legend_key.html',
      'tracing/ui/base/color_legend.html',
      'tracing/ui/base/column_chart.html',
      'tracing/ui/base/constants.html',
      'tracing/ui/base/container_that_decorates_its_children.html',
      'tracing/ui/base/d3.html',
      'tracing/ui/base/deep_utils.html',
      'tracing/ui/base/dom_helpers.html',
      'tracing/ui/base/drag_handle.html',
      'tracing/ui/base/draw_helpers.html',
      'tracing/ui/base/dropdown.html',
      'tracing/ui/base/elided_cache.html',
      'tracing/ui/base/event_presenter.html',
      'tracing/ui/base/fast_rect_renderer.html',
      'tracing/ui/base/favicons.html',
      'tracing/ui/base/file.html',
      'tracing/ui/base/grouping_table.html',
      'tracing/ui/base/grouping_table_groupby_picker.html',
      'tracing/ui/base/heading.html',
      'tracing/ui/base/hot_key.html',
      'tracing/ui/base/hotkey_controller.html',
      'tracing/ui/base/info_bar.html',
      'tracing/ui/base/info_bar_group.html',
      'tracing/ui/base/line_chart.html',
      'tracing/ui/base/list_view.html',
      'tracing/ui/base/mouse_mode_icon.html',
      'tracing/ui/base/mouse_mode_selector.html',
      'tracing/ui/base/mouse_modes.html',
      'tracing/ui/base/mouse_tracker.html',
      'tracing/ui/base/name_bar_chart.html',
      'tracing/ui/base/name_column_chart.html',
      'tracing/ui/base/name_line_chart.html',
      'tracing/ui/base/overlay.html',
      'tracing/ui/base/polymer_postload.html',
      'tracing/ui/base/polymer_preload.html',
      'tracing/ui/base/quad_stack_view.html',
      'tracing/ui/base/radio_picker.html',
      'tracing/ui/base/tab_view.html',
      'tracing/ui/base/table.html',
      'tracing/ui/base/timing_tool.html',
      'tracing/ui/base/toolbar_button.html',
      'tracing/ui/base/ui.html',
      'tracing/ui/base/ui_state.html',
      'tracing/ui/base/utils.html',
      'tracing/ui/brushing_state.html',
      'tracing/ui/brushing_state_controller.html',
      'tracing/ui/extras/about_tracing/about_tracing.html',
      'tracing/ui/extras/about_tracing/inspector_connection.html',
      'tracing/ui/extras/about_tracing/inspector_tracing_controller_client.html',
      'tracing/ui/extras/about_tracing/profiling_view.html',
      'tracing/ui/extras/about_tracing/record_controller.html',
      'tracing/ui/extras/about_tracing/record_selection_dialog.html',
      'tracing/ui/extras/about_tracing/tracing_controller_client.html',
      'tracing/ui/extras/about_tracing/xhr_based_tracing_controller_client.html',
      'tracing/ui/extras/chrome/cc/cc.html',
      'tracing/ui/extras/chrome/cc/display_item_debugger.html',
      'tracing/ui/extras/chrome/cc/display_item_list_item.html',
      'tracing/ui/extras/chrome/cc/display_item_list_view.html',
      'tracing/ui/extras/chrome/cc/layer_picker.html',
      'tracing/ui/extras/chrome/cc/layer_tree_host_impl_view.html',
      'tracing/ui/extras/chrome/cc/layer_tree_quad_stack_view.html',
      'tracing/ui/extras/chrome/cc/layer_view.html',
      'tracing/ui/extras/chrome/cc/picture_debugger.html',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_summary_view.html',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_view.html',
      'tracing/ui/extras/chrome/cc/picture_ops_list_view.html',
      'tracing/ui/extras/chrome/cc/picture_view.html',
      'tracing/ui/extras/chrome/cc/raster_task_selection.html',
      'tracing/ui/extras/chrome/cc/raster_task_view.html',
      'tracing/ui/extras/chrome/cc/selection.html',
      'tracing/ui/extras/chrome/cc/tile_view.html',
      'tracing/ui/extras/chrome/gpu/gpu.html',
      'tracing/ui/extras/chrome/gpu/state_view.html',
      'tracing/ui/extras/chrome/layout_tree_sub_view.html',
      'tracing/ui/extras/chrome_config.html',
      'tracing/ui/extras/full_config.html',
      'tracing/ui/extras/lean_config.html',
      'tracing/ui/extras/side_panel/alerts_side_panel.html',
      'tracing/ui/extras/side_panel/frame_data_side_panel.html',
      'tracing/ui/extras/side_panel/input_latency_side_panel.html',
      'tracing/ui/extras/system_stats/system_stats.html',
      'tracing/ui/extras/system_stats/system_stats_instance_track.html',
      'tracing/ui/extras/system_stats/system_stats_snapshot_view.html',
      'tracing/ui/extras/systrace_config.html',
      'tracing/ui/extras/v8/gc_objects_stats_table.html',
      'tracing/ui/extras/v8/ic_stats_table.html',
      'tracing/ui/extras/v8/multi_v8_gc_stats_thread_slice_sub_view.html',
      'tracing/ui/extras/v8/multi_v8_ic_stats_thread_slice_sub_view.html',
      'tracing/ui/extras/v8/multi_v8_thread_slice_sub_view.html',
      'tracing/ui/extras/v8/runtime_call_stats_table.html',
      'tracing/ui/extras/v8/single_v8_gc_stats_thread_slice_sub_view.html',
      'tracing/ui/extras/v8/single_v8_ic_stats_thread_slice_sub_view.html',
      'tracing/ui/extras/v8/single_v8_thread_slice_sub_view.html',
      'tracing/ui/extras/v8_config.html',
      'tracing/ui/find_control.html',
      'tracing/ui/find_controller.html',
      'tracing/ui/null_brushing_state_controller.html',
      'tracing/ui/scripting_control.html',
      'tracing/ui/side_panel/file_size_stats_side_panel.html',
      'tracing/ui/side_panel/metrics_side_panel.html',
      'tracing/ui/side_panel/side_panel.html',
      'tracing/ui/side_panel/side_panel_container.html',
      'tracing/ui/side_panel/side_panel_registry.html',
      'tracing/ui/timeline_display_transform.html',
      'tracing/ui/timeline_display_transform_animations.html',
      'tracing/ui/timeline_interest_range.html',
      'tracing/ui/timeline_track_view.html',
      'tracing/ui/timeline_view.html',
      'tracing/ui/timeline_view_help_overlay.html',
      'tracing/ui/timeline_view_metadata_overlay.html',
      'tracing/ui/timeline_viewport.html',
      'tracing/ui/tracks/alert_track.html',
      'tracing/ui/tracks/async_slice_group_track.html',
      'tracing/ui/tracks/chart_point.html',
      'tracing/ui/tracks/chart_series.html',
      'tracing/ui/tracks/chart_series_y_axis.html',
      'tracing/ui/tracks/chart_track.html',
      'tracing/ui/tracks/chart_transform.html',
      'tracing/ui/tracks/container_to_track_map.html',
      'tracing/ui/tracks/container_track.html',
      'tracing/ui/tracks/counter_track.html',
      'tracing/ui/tracks/cpu_track.html',
      'tracing/ui/tracks/cpu_usage_track.html',
      'tracing/ui/tracks/device_track.html',
      'tracing/ui/tracks/drawing_container.html',
      'tracing/ui/tracks/event_to_track_map.html',
      'tracing/ui/tracks/frame_track.html',
      'tracing/ui/tracks/global_memory_dump_track.html',
      'tracing/ui/tracks/interaction_track.html',
      'tracing/ui/tracks/kernel_track.html',
      'tracing/ui/tracks/letter_dot_track.html',
      'tracing/ui/tracks/memory_dump_track_util.html',
      'tracing/ui/tracks/memory_track.html',
      'tracing/ui/tracks/model_track.html',
      'tracing/ui/tracks/multi_row_track.html',
      'tracing/ui/tracks/object_instance_group_track.html',
      'tracing/ui/tracks/object_instance_track.html',
      'tracing/ui/tracks/other_threads_track.html',
      'tracing/ui/tracks/power_series_track.html',
      'tracing/ui/tracks/process_memory_dump_track.html',
      'tracing/ui/tracks/process_summary_track.html',
      'tracing/ui/tracks/process_track.html',
      'tracing/ui/tracks/process_track_base.html',
      'tracing/ui/tracks/rect_track.html',
      'tracing/ui/tracks/sample_track.html',
      'tracing/ui/tracks/slice_group_track.html',
      'tracing/ui/tracks/slice_track.html',
      'tracing/ui/tracks/spacing_track.html',
      'tracing/ui/tracks/stacked_bars_track.html',
      'tracing/ui/tracks/thread_track.html',
      'tracing/ui/tracks/track.html',
      'tracing/ui/tracks/x_axis_track.html',
      'tracing/ui/view_specific_brushing_state.html',
      'tracing/value/csv_builder.html',
      'tracing/value/diagnostics/add_related_names.html',
      'tracing/value/diagnostics/all_diagnostics.html',
      'tracing/value/diagnostics/breakdown.html',
      'tracing/value/diagnostics/collected_related_event_set.html',
      'tracing/value/diagnostics/date_range.html',
      'tracing/value/diagnostics/diagnostic.html',
      'tracing/value/diagnostics/diagnostic_map.html',
      'tracing/value/diagnostics/diagnostic_ref.html',
      'tracing/value/diagnostics/event_ref.html',
      'tracing/value/diagnostics/generic_set.html',
      'tracing/value/diagnostics/grouping_path.html',
      'tracing/value/diagnostics/histogram_ref.html',
      'tracing/value/diagnostics/related_event_set.html',
      'tracing/value/diagnostics/related_histogram_breakdown.html',
      'tracing/value/diagnostics/related_histogram_map.html',
      'tracing/value/diagnostics/reserved_names.html',
      'tracing/value/diagnostics/scalar.html',
      'tracing/value/diagnostics/tag_map.html',
      'tracing/value/diagnostics/unmergeable_diagnostic_set.html',
      'tracing/value/histogram.html',
      'tracing/value/histogram_grouping.html',
      'tracing/value/histogram_parameter_collector.html',
      'tracing/value/histogram_set.html',
      'tracing/value/histogram_set_hierarchy.html',
      'tracing/value/ui/breakdown_span.html',
      'tracing/value/ui/collected_related_event_set_span.html',
      'tracing/value/ui/date_range_span.html',
      'tracing/value/ui/diagnostic_map_table.html',
      'tracing/value/ui/diagnostic_span.html',
      'tracing/value/ui/diagnostic_span_behavior.html',
      'tracing/value/ui/generic_set_span.html',
      'tracing/value/ui/histogram_set_controls.html',
      'tracing/value/ui/histogram_set_table.html',
      'tracing/value/ui/histogram_set_table_cell.html',
      'tracing/value/ui/histogram_set_table_name_cell.html',
      'tracing/value/ui/histogram_set_table_row.html',
      'tracing/value/ui/histogram_set_view.html',
      'tracing/value/ui/histogram_set_view_state.html',
      'tracing/value/ui/histogram_span.html',
      'tracing/value/ui/preferred_display_unit.html',
      'tracing/value/ui/related_event_set_span.html',
      'tracing/value/ui/related_histogram_map_span.html',
      'tracing/value/ui/scalar_context_controller.html',
      'tracing/value/ui/scalar_diagnostic_span.html',
      'tracing/value/ui/scalar_map_table.html',
      'tracing/value/ui/scalar_span.html',
      'tracing/value/ui/tag_map_span.html',
      'tracing/value/ui/unmergeable_diagnostic_set_span.html',
    ],
    'tracing_img_files': [
      'tracing/ui/extras/chrome/cc/images/input-event.png',
      'tracing/ui/extras/chrome/gpu/images/checkerboard.png',
      'tracing/ui/images/chrome-left.png',
      'tracing/ui/images/chrome-mid.png',
      'tracing/ui/images/chrome-right.png',
      'tracing/ui/images/ui-states.png',
    ],
    'tracing_files': [
      '<@(tracing_css_files)',
      '<@(tracing_js_html_files)',
      '<@(tracing_img_files)',
    ],
  }
}